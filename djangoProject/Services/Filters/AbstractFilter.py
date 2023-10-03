from abc import ABC, abstractmethod


class AbstractFilter(ABC):

    @abstractmethod
    def key(self):
        pass


    @abstractmethod
    def apply(self, query, requestFilterValue, index=None):
        pass


    def requestValue(self, requestFilterValue, index=None):
        return requestFilterValue.get(f"{self.requestValueName(index)}")

    def requestValueName(self, index=None):
        index = "." + index if index is not None else ''
        return f"filters.{self.key()}{index}"