# Generated by Django 2.1.2 on 2018-11-02 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('device_id', models.CharField(max_length=100)),
                ('battery', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pressure', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
