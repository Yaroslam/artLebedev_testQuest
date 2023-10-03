from Services.Filters.AbstractFilter import AbstractFilter

class LivingPlaceFilter(AbstractFilter):

    def key(self):
        return 'living_place'

    def apply(self, query, requestFilterValue):
        return query.filter(living_place__icontains=self.requestValue(requestFilterValue)) if self.requestValue(requestFilterValue) != None else query
