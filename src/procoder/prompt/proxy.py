from typing import overload

from procoder.utils.my_typing import *

from .base import TS, Module, T, as_module


class AddIndentProxy(Module):
    """Proxy to add indent."""

    _modules: Dict[str, T]

    def __init__(self, module: T, indent: str):
        super().__init__()
        self.add_module("prompt", as_module(module))
        self._delta = indent

    def forward(self, newline=True, indent="", x=None):
        return self.prompt(newline, indent + self._delta, x)


class SilenceProxy(Module):
    """Proxy to silence the output."""

    _modules: Dict[str, T]

    def __init__(self, module: T):
        super().__init__()
        self.add_module("prompt", as_module(module))

    def forward(self, newline=True, indent="", x=None):
        return ""
