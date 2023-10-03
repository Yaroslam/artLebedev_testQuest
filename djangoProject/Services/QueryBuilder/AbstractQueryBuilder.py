from abc import ABC, abstractmethod


class AbstractQueryBuilder(ABC):
    def __init__(self, targetModel):
        self.targetModel = targetModel
        self.query = self.targetModel.objects.all()

    @abstractmethod
    def orderBy(self, *orderParams):
        pass

    @abstractmethod
    def filtering(self, filterKeys):
        pass

    def apply(self):
        return self.query

    def getByPk(self, pk):
        self.query = self.query.get(pk=pk)
        return self
