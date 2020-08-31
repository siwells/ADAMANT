import gc
from flask import Flask, jsonify
from flask import request
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

import controllers.GameController
from controllers.DatabaseController import DatabaseController
from controllers.LoggingController import LoggingController
from exception.ExceptionHandler import ExceptionHandler
from factory.GameFactory import *
from model.Dialogue import Dialogue
from model.GameStatus import GameStatus
from serializers.Serializer import DialogueSerializer, GameStatusSerializer

app = Flask(__name__)


def main():
    try:
        app.run()
    except Exception as err:
        code = err.args[0] if len(err.args) > 1 else 500
        message = err.args[1] if len(err.args) > 1 else err.args[0]
        raise ExceptionHandler(message, code)


def start_dialogue(game_id: str, game_status: GameStatus = None):
    game_fac = GameFactory()
    game_from_db, error = get_game_from_db(game_id)
    if error is not None:
        return None, error
    input_stream = InputStream(game_from_db.dialogueDescription)
    game = game_fac.create_game(input_stream)
    if game_status is not None:
        game_status.set_game_template(game)
    game_controller = controllers.GameController.GameController(game_tmp=game, dialogueId=game_id,
                                                                game_status=game_status)
    try:
        response, error = game_controller.play()
    except Exception as err:
        code = err.args[0] if len(err.args) > 1 else 500
        message = err.args[1] if len(err.args) > 1 else err.args[0]
        response = jsonify(code=code, message=message), code
        LoggingController.logger.debug("Error: ", err)
    return response, error


def get_game_from_db(game_id: str):
    error = None
    dg = None
    try:
        """@:var Dialogue dg"""
        dg = db_controller.session.query(Dialogue).filter(Dialogue.id == game_id).one()
    except NoResultFound:
        error = ExceptionHandler('ENTITY_NOT_FOUND', 404)
    except MultipleResultsFound:
        error = ExceptionHandler('MULTIPLE_ENTITIES_WITH_SAME_ID', 500)
    return dg, error


with app.app_context():
    db_controller = DatabaseController()

    @app.teardown_request
    def teardown_request(exception):
        if db_controller is not None:
            db_controller.session.close()
        gc.collect()

    @app.errorhandler(ExceptionHandler)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


    @app.route("/utterance", methods=['POST'])
    def locution():
        data = request.get_json()
        if 'dialogueId' not in data:
            raise ExceptionHandler("DIALOGUE_ID_MUST_BE_SUPPLIED", 400)
        if 'utterance' not in data:
            raise ExceptionHandler("UTTERANCE_MUST_BE_SUPPLIED", 400)
        try:
            game_status = None
            if 'gameStatus' in data:
                game_status = data.get('gameStatus')
                game_status = GameStatusSerializer().deserialize(game_status)
            utterance, error = start_dialogue(data.get('dialogueId'), game_status)
            if error is not None:
                return jsonify(message=error.message, payload=error.payload), error.status_code
            return utterance.gameStatusSerialized
        except Exception as err:
            code = err.args[0] if len(err.args) > 1 else 500
            message = err.args[1] if len(err.args) > 1 else err.args[0]
            raise ExceptionHandler(message, code)


    @app.route("/dialogue", methods=['POST', 'GET'])
    def dialogue():
        if request.method == 'GET':
            dialogue_repo = db_controller.session.query(Dialogue).all()
            response = []
            for dg in dialogue_repo:
                response.append(DialogueSerializer().serialize(dg))
            return jsonify(dialogues=response)
        elif request.method == 'POST':
            data = request.json
            if 'id' not in data or 'dialogueDescription' not in data:
                raise ExceptionHandler("PARAMS_MISSING", 400)
            # check if exists already
            dg = db_controller.session.query(Dialogue).filter(Dialogue.id == data.get('id')).first()
            if dg is not None:
                raise ExceptionHandler("ENTITY_EXISTS_CANNOT_CREATE", 409)
            dg = DialogueSerializer().deserialize(data)
            db_controller.session.add(dg)
            db_controller.session.commit()
            resp = DialogueSerializer().serialize(dg)
            return jsonify({'response': resp}), 201


    @app.route("/dialogue/<id>", methods=['GET'])
    def check_dialogue(id):
        game, error = get_game_from_db(id)
        if error is not None:
            raise error
        return jsonify(id=game.id, description=game.dialogueDescription)


    @app.route("/dialogue/<id>", methods=['DELETE'])
    def delete_dialogue(id):
        game = db_controller.session.query(Dialogue).filter(Dialogue.id == id).first()
        if game is None:
            raise ExceptionHandler('ENTITY_NOT_FOUND', 404)
        db_controller.session.delete(game)
        db_controller.session.commit()
        return jsonify()


if __name__ == '__main__':
    main()
