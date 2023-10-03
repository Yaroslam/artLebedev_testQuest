class Sorter:

    @staticmethod
    def run(query, requestOrderValue):
        orderBy = requestOrderValue.get("sort")
        if orderBy != None:
            orderColumns = orderBy.split(";")
            query = query.order_by(*orderColumns)
        return query