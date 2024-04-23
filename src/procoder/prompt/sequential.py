from typing import overload

from procoder.utils.my_typing import *

from .base import TS, Module, T, as_module
from .utils import *


class Sequential(Module):
    """A sequential combination of multiple modules."""

    _modules: Dict[str, Module]
    _indexing_method: Callable[[int], str] = None
    _name_enabled: bool = False

    @overload
    def __init__(self, *args: Module) -> None:
        ...

    @overload
    def __init__(self, arg: OrderedDict[str, Module]) -> None:
        ...

    def __init__(self, *args):
        super().__init__()
        if len(args) == 1 and isinstance(args[0], OrderedDict):
            for key, val in args[0].items():
                self.add_module(key, as_module(val))
        else:
            # if len(args) == 1 and isinstance(args[0], str):
            #     print(
            #         "Warning[PromptCoder]: Only one string is passed to "
            #         "a Sequential Module, did you forget to add commas? "
            #         f'The first 20 chars of the string argument are: "{args[0][:20]}".'
            #     )
            for idx, val in enumerate(args):
                if val is None:
                    continue
                v = as_module(val)
                key = v.refname or f"_{idx}"
                self.add_module(key, v)
        self._sep = "\n"
        self._post_init()

    def _post_init(self):
        pass

    def enable_name(self):
        self._name_enabled = True
        return self

    @property
    def indexing_method(self):
        return self._indexing_method

    @property
    def name_enabled(self):
        return self._name_enabled

    def set_indexing_method(self, func: Callable[[int], str]):
        self._indexing_method = func
        return self

    def forward(self, newline=True, indent="", x=None):
        indent += self._delta_indent
        sep = self._sep
        res = []
        for i, (k, p) in enumerate(self.named_children()):
            if i > 0:
                res.append(sep)

            # compute prefix based on indexing method and naming method
            prefix = ""
            if self.indexing_method:
                prefix += self.indexing_method(i)
            if self.name_enabled:
                prefix += f"{k}: "
            if prefix != "":
                if newline:
                    prefix = indent + prefix
                newline = False
            # combine prefix and content
            res.append(prefix + p(newline, indent, x))
            newline = sep.endswith("\n")
        return "".join(res)
