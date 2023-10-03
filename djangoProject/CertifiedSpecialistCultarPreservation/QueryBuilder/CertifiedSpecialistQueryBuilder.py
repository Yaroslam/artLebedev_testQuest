from Services.QueryBuilder.AbstractQueryBuilder import AbstractQueryBuilder
from django.apps import apps
from ..models.CertifiedSpecialist import CertifiedSpecialist
from Services.Ordering.Sorter import Sorter

class CertifiedSpecialistQueryBuilder(AbstractQueryBuilder):
    def filtering(self, filterKeys):
        for filter in apps.get_app_config('CertifiedSpecialistCultarPreservation').filterManger.getFilters(CertifiedSpecialist._meta.model_name):
            self.query = filter.apply(self.query, filterKeys)
        return self

    def orderBy(self, ordedingKeys):
        self.query = Sorter.run(self.query, ordedingKeys)
        return self
