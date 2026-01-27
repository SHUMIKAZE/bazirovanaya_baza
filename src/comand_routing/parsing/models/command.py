from typing import List, Optional

from ..models.flags import Flag


class Command:

    def __init__(
        self,
        name: Optional[str] = None,
        flags: Optional[List[Flag]] = None,
        arguments: Optional[List[str]] = None,
    ):
        self.name = name
        self.flags = flags
        self.arguments = arguments

    @property
    def has_name(self) -> bool:
        return self.name is not None