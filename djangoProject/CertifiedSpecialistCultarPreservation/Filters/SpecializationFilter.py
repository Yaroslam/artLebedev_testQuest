from Services.Filters.AbstractFilter import AbstractFilter

class SpecializationFilter(AbstractFilter):

    def key(self):
        return 'specialization'

    def apply(self, query, requestFilterValue):
        return query.filter(specialization__icontains=self.requestValue(requestFilterValue)) if self.requestValue(requestFilterValue) != None else query
