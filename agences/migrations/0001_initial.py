# Generated by Django 4.0.4 on 2022-05-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('IdAgence', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('emplacement', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('Tel', models.CharField(max_length=13)),
            ],
        ),
    ]
