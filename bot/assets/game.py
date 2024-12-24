from dataclasses import dataclass

from bot.utils.attributed_dict import AttributedDict


@dataclass
class Game:
    chat_id: int
    is_started: bool = False

    @classmethod
    def from_response(
            cls,
            response: AttributedDict
    ) -> 'Game':
        return cls(
            response.get("chat_id"),
            is_started=response.get("is_started")
        )
