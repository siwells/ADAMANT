from enum import Enum


class HandlerType(Enum):
    PRE_MOVE_CHECK = 1
    MOVE = 2
    POST_MOVE_CHECK = 3
