from aiogram.exceptions import DetailedAiogramError


class ServerError(DetailedAiogramError):
    def __init__(self):
        super().__init__("Failed to connect to server")
