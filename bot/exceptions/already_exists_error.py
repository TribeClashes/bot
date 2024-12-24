from aiogram.exceptions import DetailedAiogramError


class AlreadyExistsError(DetailedAiogramError):
    def __init__(self):
        super().__init__("Specified object already exists")
