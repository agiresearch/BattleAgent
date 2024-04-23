from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Mapping,
    NamedTuple,
    Optional,
    OrderedDict,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)


def typename(o):
    module = ""
    class_name = ""
    if (
        hasattr(o, "__module__")
        and o.__module__ != "builtins"
        and o.__module__ != "__builtin__"
        and o.__module__ is not None
    ):
        module = o.__module__ + "."

    if hasattr(o, "__qualname__"):
        class_name = o.__qualname__
    elif hasattr(o, "__name__"):
        class_name = o.__name__
    else:
        class_name = o.__class__.__name__

    return module + class_name
