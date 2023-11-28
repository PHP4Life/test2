from abc import ABC, abstractmethod


class Tech(ABC):

    @abstractmethod
    def activate(self):
        pass

    def deactivate(self):
        pass
