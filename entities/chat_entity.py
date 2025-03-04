from dataclasses import dataclass
from typing import Literal


@dataclass
class ChatMessageEntity:
    rule: Literal["user", "ai"]
    content: str
