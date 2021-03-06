# Generated by Django 2.2.4 on 2020-12-30 15:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_info', '0005_auto_20201230_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings_id',
        ),
        migrations.CreateModel(
            name='pizza_toppings',
            fields=[
                ('pizza_toppings_id', models.AutoField(primary_key=True, serialize=False)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('pizza_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza')),
                ('toppings_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_info.toppings')),
            ],
        ),
    ]
