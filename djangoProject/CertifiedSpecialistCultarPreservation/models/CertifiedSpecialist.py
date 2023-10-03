from django.db import models


class CertifiedSpecialist(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.TextField()
    living_place = models.TextField()
    specialization = models.TextField()
    category = models.TextField()
    category_order = models.TextField()
    email = models.TextField()
    phonenumber = models.TextField()


    class Meta:
        db_table = 'certified_specialist_cultar_objects_preservation'