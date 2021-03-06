# Generated by Django 3.1.6 on 2021-02-17 19:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('discription', models.TextField(blank=True)),
                ('created', models.DateField(default=datetime.datetime(2021, 2, 17, 19, 55, 38, 523882, tzinfo=utc))),
                ('category', models.ForeignKey(default='Primary', on_delete=django.db.models.deletion.DO_NOTHING, to='todo.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
