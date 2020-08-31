from concrete.artifacts import Artifact
from helpers.JsonSerializer import JsonSerializer
from model import Dialogue, InteractionMove, GameStatus, Move, Condition


class MoveSerializer(JsonSerializer):
    __attributes__ = ['name', 'final']
    __required__ = []
    __attribute_serializer__ = dict(conditions='conditions', effects='effects')
    __object_class__ = Move.Move

    def __init__(self):
        self.serializers['effects'] = dict(
            serialize=lambda x:
            [EffectSerializer().serialize(xx) for xx in x],
            deserialize=lambda x:
            [EffectSerializer().deserialize(xx) for xx in x]
        )
        self.serializers['conditions'] = dict(
            serialize=lambda x:
            [ConditionSerializer().serialize(xx) for xx in x],
            deserialize=lambda x:
            [ConditionSerializer().deserialize(xx) for xx in x]
        )


class ArtifactSerializer(JsonSerializer):
    __attributes__ = ['data', 'artifactKey']
    __required__ = []
    __attribute_serializer__ = dict()
    __object_class__ = Artifact.Artifact


class DialogueSerializer(JsonSerializer):
    __attributes__ = ['id', 'dialogueDescription']
    __required__ = ['id', 'dialogueDescription']
    __attribute_serializer__ = dict()
    __object_class__ = Dialogue.Dialogue


class InteractionMoveSerializer(JsonSerializer):
    __attributes__ = ['relativeId', 'playerName', 'moveName', 'artifact', 'role', 'final']
    __required__ = []
    __attribute_serializer__ = dict(artifact='artifact')
    __object_class__ = InteractionMove.InteractionMove

    def __init__(self):
        self.serializers['artifact'] = dict(
            serialize=lambda x:
            ArtifactSerializer().serialize(x),
            deserialize=lambda x:
            ArtifactSerializer().deserialize(x)
        )


class GameStatusSerializer(JsonSerializer):
    __attributes__ = ['id', 'dialogueId', 'last_interaction_move', 'last_move', 'mandatory_moves', 'available_moves',
                      'speakers', 'initial_turn']
    __required__ = ['id', 'dialogueId']
    __attribute_serializer__ = dict(last_interaction_move='last_interaction_move', mandatory_moves='mandatory_moves',
                                    available_moves='available_moves', past_moves='past_moves', last_move='last_move')
    __object_class__ = GameStatus.GameStatus

    def __init__(self):
        self.serializers['last_interaction_move'] = dict(
            serialize=lambda x:
            InteractionMoveSerializer().serialize(x),
            deserialize=lambda x:
            InteractionMoveSerializer().deserialize(x)
        )
        self.serializers['available_moves'] = dict(
            serialize=lambda d:
            {key: [InteractionMoveSerializer().serialize(v) for v in d[key]] for key in d.keys()},
            deserialize=lambda d:
            {key: [InteractionMoveSerializer().deserialize(v) for v in d[key]] for key in d.keys()},
        )
        self.serializers['mandatory_moves'] = dict(
            serialize=lambda d:
            {key: [InteractionMoveSerializer().serialize(v) for v in d[key]] for key in d.keys()},
            deserialize=lambda d:
            {key: [InteractionMoveSerializer().deserialize(v) for v in d[key]] for key in d.keys()},
        )
        self.serializers['past_moves'] = dict(
            serialize=lambda x:
            [InteractionMoveSerializer().serialize(xx) for xx in x],
            deserialize=lambda x:
            [InteractionMoveSerializer().deserialize(xx) for xx in x]
        )
        self.serializers['last_move'] = dict(
            serialize=lambda x:
            MoveSerializer().serialize(x),
            deserialize=lambda x:
            MoveSerializer().deserialize(x)
        )


class ConditionSerializer(JsonSerializer):
    __attributes__ = ['name', 'list']
    __required__ = []
    __attribute_serializer__ = dict()
    __object_class__ = Condition.Condition


class EffectSerializer(JsonSerializer):
    __attributes__ = ['name', 'list']
    __required__ = []
    __attribute_serializer__ = dict()
    __object_class__ = Condition.Condition
