import json
import django.db.models



class AbstractSerializer:
    data = []

    def __init__(self, querySet):
        self.querySet = querySet
        self.__serialize__()

    def __serialize__(self):
        for i in self.querySet:
            model_dict = {}
            for field in self.Meta.fields:
                field_object = self.Meta.model._meta.get_field(field)
                field_value = field_object.value_from_object(i)
                model_dict[field] = field_value
            self.data.append(model_dict)

    def get_data(self):
        self.querySet = None
        return self.data

    class Meta:
        model = django.db.models.Model
        fields = "__all__"
