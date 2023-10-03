class FilterManager:
    def __init__(self):
        self.filters = {}

    def register_filter(self, model_name, filter):
        if model_name not in self.filters.keys():
            self.filters[model_name] = []
        self.filters[model_name].append(filter)

    def getFilters(self, model_name):
        return self.filters[model_name]