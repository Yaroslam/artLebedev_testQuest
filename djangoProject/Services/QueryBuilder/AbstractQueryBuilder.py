from abc import ABC, abstractmethod
from django.core.exceptions import ObjectDoesNotExist

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
        try:
            self.query = self.query.get(pk=pk)
        except ObjectDoesNotExist:
            self.query = []
        return self
