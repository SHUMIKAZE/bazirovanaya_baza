from collections.abc import Callable
from inspect import signature, Parameter
from typing import TypeVar, get_type_hints, Any, Optional

from .command import Command

R = TypeVar("R")


class Handler:
    def __init__(
        self,
        handler_func: Callable[..., R],
    ) -> None:
        self._validate_callable(handler_func)
        # self._validate_return_class(handler_func, return_cls)

        self._handler_func = handler_func
        self._command_param: Optional[str] = None
        self._context_param: Optional[str] = None
        self._parse_signature(handler_func)

    def __call__(self, command: Command, context: Any) -> R:
        kwargs = {}
        if self._command_param:
            kwargs[self._command_param] = command
        if self._context_param:
            kwargs[self._context_param] = context
        return self._handler_func(**kwargs)

    def _parse_signature(self, func) -> None:
        sig = signature(func)
        params = list(sig.parameters.values())

        if len(params) > 2:
            raise ValueError("Обработчик должен иметь не более 2 аргументов")

        hints = get_type_hints(func)

        for param in params:
            if param.kind not in (Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD):
                raise ValueError("Аргумент обработчика должен быть позиционным")

            param_type = hints.get(param.name)

            if param_type is Command:
                if self._command_param is not None:
                    raise TypeError("Аргумент типа Command уже определен")
                self._command_param = param.name
            else:
                if self._context_param is not None:
                    raise TypeError("Аргумент контекста уже определен")
                self._context_param = param.name

    @staticmethod
    def _validate_callable(func) -> None:
        if not callable(func):
            raise TypeError(
                f"Handler must be callable, not {type(func).__name__}"
            )

    @staticmethod
    def _validate_return_class(func, expected_cls: type) -> None:
        hints = get_type_hints(func)
        actual = hints.get("return")

        if actual is None:
            raise TypeError(
                f"{func.__name__} must have a return type annotation"
            )

        is_valid = False
        try:
            is_valid = issubclass(actual, expected_cls)
        except TypeError:
            is_valid = actual is expected_cls

        if not is_valid:
            raise TypeError(
                f"{func.__name__} must return exactly "
                f"{expected_cls.__name__}, not {actual}"
            )
