# Generated by Django 2.2.4 on 2020-12-28 06:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizza_status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pizza_type',
            fields=[
                ('pizza_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza_status')),
            ],
        ),
        migrations.CreateModel(
            name='pizza_toppings',
            fields=[
                ('pizza_toppings_id', models.AutoField(primary_key=True, serialize=False)),
                ('toppings', models.CharField(blank=True, max_length=100)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza_status')),
            ],
        ),
        migrations.CreateModel(
            name='pizza_size',
            fields=[
                ('pizza_size_id', models.AutoField(primary_key=True, serialize=False)),
                ('pizza_size_name', models.CharField(blank=True, max_length=100)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza_status')),
            ],
        ),
    ]