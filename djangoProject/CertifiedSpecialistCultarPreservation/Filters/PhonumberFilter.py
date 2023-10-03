from Services.Filters.AbstractFilter import AbstractFilter

class PhonumberFilter(AbstractFilter):

    def key(self):
        return 'phone'

    def apply(self, query, requestFilterValue):
        return query.filter(phonenumber__icontains=self.requestValue(requestFilterValue)) if self.requestValue(requestFilterValue) != None else query
