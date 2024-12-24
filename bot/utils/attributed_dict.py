from typing import Any


class AttributedDict(dict):
    def __init__(
            self,
            dictionary: dict,
            **kwargs
    ) -> None:
        super().__init__(dictionary, **kwargs)

        for key, value in dictionary.items():
            setattr(self, str(key), self.__process_value__(value))

    def __getattr__(
            self,
            item: str
    ) -> Any:
        return self.__dict__.get(item)

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def __process_value__(
            self,
            value: Any
    ) -> Any:
        if isinstance(value, dict):
            return AttributedDict(value)

        if isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set):
            return [self.__process_value__(item) for item in value]

        return value
