from functools import partial

from procoder.utils.my_typing import *
from procoder.utils.my_typing import Any, Dict

from .base import TS, Module, T, as_module
from .sequential import *
from .utils import make_ordered_dict


class Paired(Sequential):
    """A pair of modules"""

    def __init__(self, first: TS, second: TS):
        super().__init__(make_ordered_dict(["first", "second"], [first, second]))

    def _post_init(self):
        self._sep = " "


class Collection(Sequential):
    """A collection of multiple modules, seperated by newlines."""

    def _post_init(self):
        self.set_indexing_method(number_indexing)


class Block(Sequential):
    """A prompt block."""

    def __init__(self, head: TS, body: TS):
        super().__init__(make_ordered_dict(["head", "body"], [head, body]))


class NamedBlock(Sequential):
    """A named prompt block.

    Args:
        name: Name of the block.
        content: Content of the block.
        refname: the name to reference the block.
        shortname: Short name of the block, used when referenced.
    """

    def __init__(self, name: TS, content: TS, refname: str = None):
        super().__init__(make_ordered_dict(["name", "content"], [name, content]))
        if isinstance(name, str):
            self._name = name
        self._refname = refname


class NamedVariable(NamedBlock):
    def _post_init(self):
        self._sep = ": "
