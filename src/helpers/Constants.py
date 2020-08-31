import os

NO_GAME_DESCRIPTION = "Please provide game description"
COLON = ":"
OPEN_BRACE = "{"
CLOSE_BRACE = "}"
COMMA = ","
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"
EXIT = "EXIT"
EMPTY = ""
DEBUG = True

# MoveEvaluator constants
NEXT = 'next'
NOT_NEXT = '!next'
FUTURE = 'future'
NOT_FUTURE = '!future'

# Basic roles
SPEAKER = "Speaker"
LISTENER = "Listener"

# InteractionMove json attribute keys
MOVE_ID = "moveId"
MOVE_NAME = "moveName"
ARTIFACT = "artifact"
ARTIFACT_KEY = "artifactKey"
ARTIFACT_ID = "artifactId"
ARTIFACT_DATA = "artifactData"
PLAYER_NAME = "playerName"
ROLE = "role"
FINAL = "final"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Errors
WRONG_MESSAGE_FORMAT = "WRONG_MESSAGE_FORMAT"
MESSAGE_HAS_NO_ID = "MESSAGE_HAS_NO_ID"

# routes
UTTERANCE = "utterance"
