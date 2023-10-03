from django.apps import AppConfig
from Services.Filters.FilterManager import FilterManager
from .Filters.CategoryFilter import CategoryFilter
from .Filters.EmailFilter import EmailFilter
from .Filters.FioFilter import FioFilter
from .Filters.LivingPlaceFilter import LivingPlaceFilter
from .Filters.PhonumberFilter import PhonumberFilter
from .Filters.SpecializationFilter import SpecializationFilter
from .Filters.OrderFilter import OrderFilter


class CertifiedSpecialistCultarPreservation(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CertifiedSpecialistCultarPreservation'

    def ready(self):
        from .models.CertifiedSpecialist import CertifiedSpecialist
        self.filterManger = FilterManager()
        self.filterManger.register_filter(CertifiedSpecialist._meta.model_name, CategoryFilter())
        self.filterManger.register_filter(CertifiedSpecialist._meta.model_name, EmailFilter())
        self.filterManger.register_filter(CertifiedSpecialist._meta.model_name, FioFilter())
        self.filterManger.register_filter(CertifiedSpecialist._meta.model_name, LivingPlaceFilter())
        self.filterManger.register_filter(CertifiedSpecialist._meta.model_name, PhonumberFilter())
        self.filterManger.register_filter(CertifiedSpecialist._meta.model_name, SpecializationFilter())
        self.filterManger.register_filter(CertifiedSpecialist._meta.model_name, OrderFilter())

