from Services.Filters.AbstractFilter import AbstractFilter

class FioFilter(AbstractFilter):

    def key(self):
        return 'fio'

    def apply(self, query, requestFilterValue):
        return query.filter(fio__icontains=self.requestValue(requestFilterValue)) if self.requestValue(requestFilterValue) != None else query
