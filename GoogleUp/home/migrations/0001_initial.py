# Generated by Django 3.0.1 on 2019-12-31 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('map_name', models.CharField(max_length=200)),
            ],
        ),
    ]
