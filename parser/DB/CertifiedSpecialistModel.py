from .BaseModel import BaseModel
from peewee import TextField, IntegerField


class CertifiedSpecialistModel(BaseModel):
    id = IntegerField(primary_key=True)
    fio = TextField()
    living_place = TextField()
    specialization = TextField()
    category = TextField()
    category_order = TextField()
    email = TextField()
    phonenumber = TextField()

    class Meta:
        db_table = "certified_specialist_cultar_objects_preservation"