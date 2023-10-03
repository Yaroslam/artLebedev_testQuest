from Services.Filters.AbstractFilter import AbstractFilter

class CategoryFilter(AbstractFilter):

    def key(self):
        return 'category'

    def apply(self, query, requestFilterValue):
        if self.requestValueName() in requestFilterValue:
            return query.filter(category__icontains=self.requestValue(requestFilterValue))
        else:
            return query