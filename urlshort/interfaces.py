from abc import ABCMeta, abstractmethod


class BaseSlugCreator(metaclass=ABCMeta):

    def __init__(self, length: int) -> None:
        self.length = length
        super().__init__()

    @abstractmethod
    def get_slug(self) -> str:
        pass
