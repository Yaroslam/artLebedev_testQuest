from Services.Filters.AbstractFilter import AbstractFilter

class EmailFilter(AbstractFilter):

    def key(self):
        return 'email'

    def apply(self, query, requestFilterValue):
        return query.filter(email__icontains=self.requestValue(requestFilterValue)) if self.requestValue(requestFilterValue) != None else query
