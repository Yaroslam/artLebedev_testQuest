from Services.Filters.AbstractFilter import AbstractFilter

class OrderFilter(AbstractFilter):

    def key(self):
        return 'order'

    def apply(self, query, requestFilterValue):
        number = self.requestValue(requestFilterValue, index="number")
        numberRegExp = f"№{number}"

        date = ''
        dateDay = self.requestValue(requestFilterValue, index="date.day")
        dateMounth = self.requestValue(requestFilterValue, index="date.mounth")
        dateYear = self.requestValue(requestFilterValue, index="date.year")

        if dateDay != None:
            date+=f"{dateDay}."
        if dateMounth != None:
            date+=f".{dateMounth}."
        if dateYear != None:
            date += f".{dateYear}"

        date = date.replace("..", ".")
        
        query = query.filter(
            category_order__icontains=date) if date != None else query
        query = query.filter(
            category_order__icontains=numberRegExp) if number != None else query
        return query
