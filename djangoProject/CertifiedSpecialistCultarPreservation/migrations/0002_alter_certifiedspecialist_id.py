# Generated by Django 4.1.2 on 2023-10-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CertifiedSpecialistCultarPreservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifiedspecialist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
