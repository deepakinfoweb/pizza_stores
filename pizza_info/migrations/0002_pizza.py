# Generated by Django 2.2.4 on 2020-12-30 06:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('pizza_id', models.AutoField(primary_key=True, serialize=False)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('pizza_size_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza_size')),
                ('pizza_toppings_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza_toppings')),
                ('pizza_type_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza_type')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_info.pizza_status')),
            ],
        ),
    ]
