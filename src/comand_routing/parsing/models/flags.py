from typing import Optional, ClassVar

from ..enums.parser import FlagType


class Flag:

    __flag_type__: ClassVar[FlagType]

    def __init__(
        self,
        flag_name: str,
        argument: Optional[str] = None,
    ) -> None:
        self.flag_name = flag_name
        self.argument = argument
        self._flag_type = self.__flag_type__

    @property
    def flag_type(self) -> FlagType:
        return self.__flag_type__

    @property
    def has_argument(self) -> bool:
        return self.argument is not None

class ShortFlag(Flag):
    __flag_type__ = FlagType.SHORT

class LongFlag(Flag):
    __flag_type__ = FlagType.LONG