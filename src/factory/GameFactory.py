from concrete.artifacts.Content import Content
from enums.Role import Role
from dgdl.dgdlLexer import dgdlLexer
from dgdl.dgdlListener import dgdlListener
from dgdl.dgdlParser import dgdlParser
from dgdl.dgdlVisitor import *
from helpers.Constants import *
from helpers.StringParser import StringParser
from model.Game import Game
from model.Move import Move
from model.Player import Player
from model.Principle import *
from model.Store import Store


class GameFactory(dgdlListener, dgdlVisitor):
    def __init__(self):
        self._game = Game()
        pass

    def _get_game(self) -> Game:
        return self._game

    def _set_game(self, game: Game = None):
        self._game = game

    game = property(_get_game, _set_game, None, "Game object created by factory")

    # Enter a parse tree produced by dgdlParser#game.
    def enterGame(self, ctx: dgdlParser.GameContext):
        data = str(ctx.getText())
        if str(ctx.IDENT()) in data:
            self.game.name = StringParser.before(data, OPEN_BRACE)
        if ctx.roles():
            # for role in ctx.roles():
            self.game.roles = (self.visit(ctx.roles(0)))

    # Enter a parse tree produced by dgdlParser#store.
    def enterStore(self, ctx: dgdlParser.StoreContext):
        data = str(ctx.getText())
        store = Store()
        if str(ctx.NAME()) in data:
            store.name = StringParser.between(data, str(ctx.NAME()) + COLON, COMMA)
        if str(ctx.OWNER()) in data:
            values = StringParser.between(data, str(ctx.OWNER()) + OPEN_BRACE, CLOSE_BRACE)
            store.owner = values.split(COMMA)
        if str(ctx.STRUCTURE()) in data:
            store.structure = StringParser.between(data, str(ctx.STRUCTURE()) + COLON, COMMA)
        if str(ctx.VISIBILITY()) in data:
            store.visibility = StringParser.between(data, str(ctx.VISIBILITY()) + COLON, CLOSE_BRACE)
        self.game.stores.append(store)

    # Enter a parse tree produced by dgdlParser#turns.
    def enterTurns(self, ctx: dgdlParser.TurnsContext):
        data = str(ctx.getText())
        if str(ctx.MAX()) in data:
            self.game.turns.max = int(StringParser.between(data, str(ctx.MAX()) + COLON, CLOSE_BRACE))
        if str(ctx.MAGNITUDE()) in data:
            self.game.turns.magnitude = StringParser.between(data, str(ctx.MAGNITUDE()) + COLON, COMMA)
        if str(ctx.ORDERING()) in data:
            self.game.turns.ordering = StringParser.between(data, str(ctx.ORDERING()) + COLON,
                                                            COMMA if (str(ctx.MAX()) in data) else CLOSE_BRACE)

    # Enter a parse tree produced by dgdlParser#players.
    def enterPlayers(self, ctx: dgdlParser.PlayersContext):
        data = str(ctx.getText())
        if str(ctx.MIN()) in data:
            self.game.players.min = int(
                StringParser.between(data, str(ctx.MIN()) + COLON, COMMA if (str(ctx.MAX()) in data) else CLOSE_BRACE))
        if str(ctx.MAX()) in data:
            self.game.players.max = int(StringParser.between(data, str(ctx.MAX()) + COLON, CLOSE_BRACE))

    # Enter a parse tree produced by dgdlParser#player.
    def enterPlayer(self, ctx: dgdlParser.PlayerContext):
        data = str(ctx.getText())
        player = Player()
        if str(ctx.NAME()) in data:
            player.name = StringParser.between(data, str(ctx.NAME()) + COLON,
                                               COMMA if (ctx.roles()) else CLOSE_BRACE)
        if ctx.roles():
            roles = self.visit(ctx.roles())
            player.roles = roles
        self.game.players.list.append(player)

    # Enter a parse tree produced by dgdlParser#roles.
    def enterRoles(self, ctx: dgdlParser.RolesContext):
        if (ctx.getRuleContext() == self.exitStore) or (ctx.getRuleIndex() == self.exitPlayer):
            roles = self.visit(dgdlParser.RolesContext)
            self.game.roles = roles

    # Enter a parse tree produced by dgdlParser#principle.
    def enterPrinciple(self, ctx: dgdlParser.PrincipleContext):
        principle = Principle()
        data = str(ctx.getText())
        if str(ctx.IDENT()) in data:
            principle.name = StringParser.before(data, OPEN_BRACE)
        if ctx.scope():
            principle.scope = self.visit(ctx.scope())
        if ctx.conditions():
            principle.conditions = self.visit(ctx.conditions())
        if ctx.effects():
            principle.effects = self.visit(ctx.effects())
        self.game.principles.append(principle)

    # Enter a parse tree produced by dgdlParser#moves.
    def enterMoves(self, ctx: dgdlParser.MovesContext):
        pass

    # Enter a parse tree produced by dgdlParser#move.
    def enterMove(self, ctx: dgdlParser.MoveContext):
        move = Move()
        data = str(ctx.getText())
        if str(ctx.IDENT()) in data:
            move.name = StringParser.before(data, OPEN_BRACE)
        if ctx.content():
            move.content = self.visit(ctx.content())
        if ctx.conditions():
            move.conditions = self.visit(ctx.conditions())
        if ctx.effects():
            move.effects = self.visit(ctx.effects())
        self.game.moves.append(move)

    # Visit a parse tree produced by dgdlParser#roles.
    def visitRoles(self, ctx: dgdlParser.RolesContext):
        data = str(ctx.getText())
        values = []
        if str(ctx.ROLES()) in data:
            roles = StringParser.between(data, str(ctx.ROLES()) + OPEN_BRACE, CLOSE_BRACE)
            roles_tmp = roles.split(COMMA)
            values = roles_tmp
            """for role in roles_tmp:
                if str.upper(role) == Role.LISTENER.name:
                    values.append(Role.LISTENER)
                elif str.upper(role) == Role.SPEAKER.name:
                    values.append(Role.SPEAKER)
                elif str.upper(role) == Role.RESPONDENT.name:
                    values.append(Role.RESPONDENT)
                elif str.upper(role) == Role.INITIATOR.name:
                    values.append(Role.INITIATOR)
                elif str.upper(role) == Role.LOOSER.name:
                    values.append(Role.LOOSER)
                elif str.upper(role) == Role.WINNER.name:
                    values.append(Role.WINNER)
                elif str.upper(role) == Role.PROPONENT.name:
                    values.append(Role.PROPONENT)
                elif str.upper(role) == Role.OPPONENT.name:
                    values.append(Role.OPPONENT)
                """
        return values

    # Visit a parse tree produced by dgdlParser#scope.
    def visitScope(self, ctx: dgdlParser.ScopeContext):
        data = str(ctx.getText())
        scope = None
        if str(ctx.SCOPE()) in data:
            scope = StringParser.after(data, str(ctx.SCOPE()) + COLON)
        return scope

    # Visit a parse tree produced by dgdlParser#conditions.
    def visitConditions(self, ctx: dgdlParser.ConditionsContext):
        data = str(ctx.getText())
        result = []
        if str(ctx.CONDITIONS()) in data:
            sub_str = StringParser.between(data, OPEN_BRACE, CLOSE_BRACE)
            values = sub_str.split(CLOSE_BRACKET + COMMA)
            for condition_tmp in values:
                if condition_tmp == EMPTY:
                    continue
                condition_tmp += CLOSE_BRACKET
                condition = Condition()
                condition.name = StringParser.before(condition_tmp, OPEN_BRACKET)
                conditions = StringParser.between(condition_tmp, OPEN_BRACKET, CLOSE_BRACKET)
                condition.list = conditions.split(COMMA)
                result.append(condition)
        return result

    # Visit a parse tree produced by dgdlParser#effects.
    def visitEffects(self, ctx: dgdlParser.EffectsContext):
        data = str(ctx.getText())
        result = []
        if str(ctx.EFFECTS()) in data:
            sub_str = StringParser.between(data, OPEN_BRACE, CLOSE_BRACE)
            values = sub_str.split(CLOSE_BRACKET + COMMA)
            for effect_tmp in values:
                if effect_tmp == EMPTY:
                    continue
                effect_tmp += CLOSE_BRACKET
                effect = Effect()
                effect.name = StringParser.before(effect_tmp, OPEN_BRACKET)
                effects = StringParser.between(effect_tmp, OPEN_BRACKET, CLOSE_BRACKET)
                effect.list = effects.split(",")
                result.append(effect)
        return result

    # Visit a parse tree produced by dgdlParser#content.
    def visitContent(self, ctx: dgdlParser.ContentContext):
        data = str(ctx.getText())
        content = Content()
        if str(ctx.CONTENT()) in data:
            str_tmp = StringParser.between(data, OPEN_BRACE, CLOSE_BRACE)
            content.list = str_tmp.split(COMMA)
        return content

    def create_game(self, input_stream):
        lexer = dgdlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = dgdlParser(stream)
        tree = parser.game()
        listener = self
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return self.game
