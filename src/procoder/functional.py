import copy

from procoder.utils.my_typing import *

from .prompt.base import TS, Module, Single, T, as_module
from .prompt.proxy import AddIndentProxy, SilenceProxy


def as_prompt(x: TS):
    return as_module(x)


# def flatten(x: T):

indent2 = " " * 2
indent4 = " " * 4
indent_tab = "\t"


def silence(x: T):
    return SilenceProxy(x)


def add_indent(x: T, indent: str):
    return AddIndentProxy(x, indent)


def add_indent2(x: T):
    return add_indent(x, indent=indent2)


def add_indent4(x: T):
    return add_indent(x, indent=indent4)


def add_indent_tab(x: T):
    return add_indent(x, indent=indent_tab)


def process_module_refname(v: T, target: Dict[str, Any], key: str = None):
    refname = v.refname or key
    name = v._get_name()

    if refname and name:
        if refname in target:
            raise ValueError(f"Duplicate key: {refname}")
        else:
            target[refname] = name


def collect_refnames(vars: Union[Dict[str, Any], T]) -> Dict[str, Any]:
    """Collect a mapping from refnames to names from all submodules of the vars"""
    target = {}
    modules = set()

    if isinstance(vars, Module):
        vars = {"prompt": vars}
    else:
        vars = {**vars}  # copy

    # find all submodules
    for k, v in vars.items():
        if isinstance(v, Module):
            modules |= v.get_all_submodules()

    for k, v in vars.items():
        if isinstance(v, Module):
            process_module_refname(v, target, key=k)
            # avoid duplicate
            modules.discard(v)

    for v in modules:
        process_module_refname(v, target)

    return target


def format_refnames(inputs: Dict[str, Any], format_func: Callable[[Any], str]):
    """Format the names with format_func"""
    return {k: format_func(v) for k, v in inputs.items()}


def add_brackets(refnames: Dict[str, Any]) -> Dict[str, Any]:
    return format_refnames(refnames, lambda x: f"[{x}]")


def check_duplicate_keys(x: Dict[str, Any], y: Dict[str, Any]):
    """Check if there are duplicate keys in two dicts"""
    for k in x.keys():
        if k in y:
            raise ValueError(f"Duplicate key: {k}")


def add_refnames(
    vars: Union[Dict[str, Any], T], target: Dict[str, Any], include_brackets=True
):
    """Add refnames to the target dict"""
    refnames = collect_refnames(vars)
    if include_brackets:
        refnames = add_brackets(refnames)
    check_duplicate_keys(target, refnames)
    target.update(refnames)
    return target


def format_prompt(
    prompt: Optional[TS],
    inputs: Dict[str, Any],
    refnames: Dict[str, Any] = None,
    include_brackets: bool = True,
) -> Optional[str]:
    """Format the prompt with inputs and (optional) refnames"""
    if prompt is None:
        return None
    if isinstance(prompt, str):
        return prompt
    if refnames is None:
        refnames = collect_refnames(dict(prompt=prompt))
    if include_brackets:
        refnames = add_brackets(refnames)
    check_duplicate_keys(inputs, refnames)
    return prompt(x={**inputs, **refnames})


def format_multiple_prompts(
    prompts: List[Optional[TS]],
    inputs: Dict[str, Any],
    refnames: Dict[str, Any] = None,
    include_brackets: Union[bool, List[bool]] = None,
) -> List[str]:
    """Format multiple prompts with inputs and (optional) refnames"""
    if refnames is None:
        refnames = collect_refnames(
            {
                f"prompt_{i}": prompt
                for i, prompt in enumerate(prompts)
                if prompt is not None
            }
        )
    if include_brackets is None:
        include_brackets = True
    if isinstance(include_brackets, bool):
        include_brackets = [include_brackets] * len(prompts)
    if len(prompts) != len(include_brackets):
        raise ValueError(
            f"Length of prompts ({len(prompts)}) and include_brackets ({len(include_brackets)}) should be the same"
        )

    results = []
    for prompt, include in zip(prompts, include_brackets):
        results.append(format_prompt(prompt, inputs, refnames, include))
    return results


def remove_direct_submodule(
    x: T, names: List[str] = None, refnames: List[str] = None
) -> T:
    """Remove a list of direct submodules by names or refnames"""
    if names is None and refnames is None:
        raise ValueError("Either names or refnames should be specified")
    y = copy.deepcopy(x)
    remains = OrderedDict()
    for name, module in x.named_children():
        if names is not None and name in names:
            continue
        if refnames is not None and module.refname in refnames:
            continue
        remains[name] = module
    y.set_submodules(remains)
    return y


def remove_submodule(x: T, refname: str, recursive=True) -> Tuple[T, bool]:
    """Remove a submodule [recursively] by refname"""
    y, success = x, False

    for name, module in x.named_children():
        if module.refname == refname:
            y = remove_direct_submodule(x, refnames=[refname])
            success = True
        elif recursive:
            removed, success_ = remove_submodule(module, refname, recursive)
            if success_:
                y = copy.deepcopy(x)
                y._replace_submodule(name, removed)
            success = success or success_
        if success:
            break
    return y, success


def removed_submodule(x: T, refname: str, recursive=True) -> T:
    """Remove a submodule [recursively] by refname"""
    assert isinstance(refname, str), f"refname should be a string, got {refname}"
    y, _ = remove_submodule(x, refname, recursive)
    return y


def removed_submodules(x: T, refnames: Union[List[str], str], recursive=True) -> T:
    """Remove a list of submodules [recursively] by refnames"""
    if isinstance(refnames, str):
        refnames = [refnames]
    for refname in refnames:
        x = removed_submodule(x, refname, recursive)
    return x


def replace_submodule(
    x: T, refname: str, new_module: T, recursive=True
) -> Tuple[T, bool]:
    """Replace a module [recursively] with a new module, by refname."""
    y = copy.deepcopy(x)
    success = False

    for name, module in x.named_children():
        if module.refname == refname:
            y._replace_submodule(name, new_module)
            # set new_module's refname to refname
            assert new_module.refname is None or new_module.refname == refname
            new_module.set_refname(refname)
            success = True
        elif recursive:
            replaced, success_ = replace_submodule(
                module, refname, new_module, recursive
            )
            if success_:
                y._replace_submodule(name, replaced)
            success = success or success_
        if success:
            break
    return y, success


def replaced_submodule(x: T, refname: str, new_module: T, recursive=True) -> T:
    """Replace a module [recursively] with a new module, by refname."""
    y, _ = replace_submodule(x, refname, new_module, recursive)
    return y


def find_submodule(x: T, refname: str) -> T:
    """Find a submodule by refname"""
    for module in x.get_all_submodules():
        if module.refname == refname:
            return module
    return None


def replace_prompt(x: T, replace_func: Callable[[str], str], inplace=False) -> T:
    """Replace the prompt of a module or its direct submodules by a replace function"""
    y = x if inplace else copy.deepcopy(x)
    if isinstance(y, Single):
        y.prompt = replace_func(y.prompt)
    else:
        for name, module in y.named_children():
            y._replace_submodule(name, replace_prompt(module, replace_func))
    return y
