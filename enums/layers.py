from enum import IntEnum, auto

class Layers(IntEnum):
    """ Enum of sprite layers

    Args:
        IntEnum (_type_): Int enumeration
    """
    BACKGROUND = auto()
    OBSTACLE = auto()
    PLAYER = auto()
    UI = auto()