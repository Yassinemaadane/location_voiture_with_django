# Generated by Django 4.0.4 on 2022-06-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offres', '0003_remove_offre_datedefin'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='DateDefin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='offre',
            name='DateDebut',
            field=models.DateField(null=True),
        ),
    ]
