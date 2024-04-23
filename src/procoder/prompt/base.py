from procoder.utils.my_typing import *

T = TypeVar("T", bound="Module")
TS = Union[T, str]

# Mimicing the pytorch design of nn.Module


class Module:
    r"""Base class for all prompt modules.

    Your prompts should also subclass this class.

    Modules can also contain other Modules, allowing to nest them in a tree structure. You can assign the submodules as regular attributes::

        import procoder.prompt as pp
        import procoder.prompt.functional as PF

        class Prompt(pp.Module):
            def __init__(self):
                super().__init__()
                self.prompt1 = pp.Single("What is your name?")
                self.prompt2 = pp.Single("What is your quest?")

            def repr(self, x):
                return PF.concat([self.prompt1(x), self.prompt2(x)])

    Submodules assigned in this way will be registered.

    .. note::
        As per the example above, an ``__init__()`` call to the parent class
        must be made before assignment on the child.
    """

    _modules: Dict[str, Optional["Module"]]
    _sep: str = ""
    _delta_indent: str = ""
    _name: str = None
    _refname: str = None
    _debug: bool = False

    def __init__(self, *args, **kwargs) -> None:
        super().__setattr__("_modules", OrderedDict())

    def set_sep(self, sep: str) -> "Module":
        self._sep = sep
        return self

    def set_delta_indent(self, delta_indent: str) -> "Module":
        self._delta_indent = delta_indent
        return self

    def set_refname(self, refname: str) -> "Module":
        self._refname = refname
        return self

    def forward(
        self, newline: bool = True, indent: str = "", x: Dict[str, Any] = None
    ) -> TS:
        """Forward pass of the module.

        Args:
            newline: Whether this is a beginning of a new line.
            indent: Indentation string.
            x: Input to the module.

        Returns:
            Output of the module.
        """
        raise NotImplementedError

    def _call_impl(self, *args, **kwargs):
        if self._debug:
            print(f"entered {self} with refname={self.refname}")
        return self.forward(*args, **kwargs)

    __call__: Callable[..., Any] = _call_impl

    def add_module(self, name: str, module: Optional["Module"]) -> None:
        r"""Adds a child module to the current module.

        The module can be accessed as an attribute using the given name.

        Args:
            name (str): name of the child module. The child module can be
                accessed from this module using the given name
            module (Module): child module to be added to the module.
        """
        if not isinstance(module, Module) and module is not None:
            raise TypeError("{} is not a Module subclass".format(typename(module)))
        elif not isinstance(name, str):
            raise TypeError(
                "module name should be a string. Got {}".format(typename(name))
            )
        elif hasattr(self, name) and name not in self._modules:
            raise KeyError("attribute '{}' already exists".format(name))
        elif "." in name:
            raise KeyError('module name can\'t contain ".", got: {}'.format(name))
        elif name == "":
            raise KeyError('module name can\'t be empty string ""')
        self._modules[name] = module

    def _replace_submodule(self, name: str, module: Optional["Module"]) -> None:
        """Replace one of the submodule of this module by name."""
        if not isinstance(module, Module) and module is not None:
            raise TypeError("{} is not a Module subclass".format(typename(module)))
        if name not in self._modules:
            raise KeyError("attribute '{}' not exists".format(name))
        self._modules[name] = module

    def set_submodules(self, modules: Dict[str, Optional["Module"]]) -> None:
        """Sets the submodules of this module."""
        for name, module in modules.items():
            if not isinstance(module, Module) and module is not None:
                raise TypeError("{} is not a Module subclass".format(typename(module)))
        self._modules = modules

    def get_submodule(self, target: str) -> "Module":
        """
        Returns the submodule given by ``target`` if it exists,
        otherwise throws an error.

        Args:
            target: The fully-qualified string name of the submodule
                to look for.

        Returns:
            Module: The submodule referenced by ``target``

        Raises:
            AttributeError: If the target string references an invalid
                path or resolves to something that is not an
                ``Module``
        """
        if target == "":
            return self

        atoms: List[str] = target.split(".")
        mod: "Module" = self

        for item in atoms:
            if not hasattr(mod, item):
                raise AttributeError(
                    mod._get_name() + " has no " "attribute `" + item + "`"
                )

            mod = getattr(mod, item)

            if not isinstance(mod, Module):
                raise AttributeError("`" + item + "` is not " "an Module")

        return mod

    @property
    def refname(self):
        return self._refname

    def _get_name(self):
        if self._name:
            return self._name
        return self.__class__.__name__

    def __getattr__(self, name: str) -> "Module":
        if "_modules" in self.__dict__:
            modules = self.__dict__["_modules"]
            if name in modules:
                return modules[name]
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(type(self).__name__, name)
            )
        else:  # to support copy
            return object.__getattribute__(self, name)

    def children(self) -> Iterator["Module"]:
        r"""Returns an iterator over immediate children modules.

        Yields:
            Module: a child module
        """
        for name, module in self.named_children():
            yield module

    def named_children(self) -> Iterator[Tuple[str, "Module"]]:
        r"""Returns an iterator over immediate children modules, yielding both
        the name of the module as well as the module itself.

        Yields:
            (str, Module): Tuple containing a name and child module
        """
        memo = set()
        for name, module in self._modules.items():
            if module is not None and module not in memo:
                memo.add(module)
                yield name, module

    def get_all_submodules(self) -> Set["Module"]:
        r"""Returns an iterator over all submodules.

        Yields:
            Module: a submodule
        """
        modules = set()
        for module in self.children():
            modules.add(module)
            modules |= module.get_all_submodules()
        return modules


class Single(Module):
    def __init__(self, prompt: str, need_format: bool = True):
        super().__init__()
        self.prompt = prompt
        self._need_format = need_format

    def forward(self, newline: bool = True, indent: str = "", x: Dict[str, Any] = None):
        content = self.prompt
        if self._need_format and x is not None:
            content = content.format(**x)
        return indent + content if newline else content


def as_module(x: TS):
    if isinstance(x, Module):
        return x
    elif isinstance(x, str):
        return Single(x)
    else:
        raise TypeError(f"Expected Module or str, but got {type(x)}")
