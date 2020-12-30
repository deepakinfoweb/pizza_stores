from django.db import models
from datetime import datetime,timedelta

class pizza_status(models.Model):
    status_id = models.AutoField(primary_key=True) #1=> Active, 2=> inactive
    status_name = models.CharField(max_length =100, default = None, null=True)
    def __str__(self):
        return str(self.status_id)

class pizza_type(models.Model):
    pizza_type_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(pizza_status, on_delete=models.CASCADE, default = 1)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.pizza_type_id)

class pizza_size(models.Model):
    pizza_size_id=models.AutoField(primary_key=True)
    pizza_size_name = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(pizza_status, on_delete=models.CASCADE, default = 1)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.pizza_size_id)


class toppings(models.Model):
    toppings_id=models.AutoField(primary_key=True)
    toppings = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(pizza_status, on_delete=models.CASCADE, default = 1)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.toppings_id)

class pizza(models.Model):
    pizza_id=models.AutoField(primary_key=True)
    pizza_type_id= models.ForeignKey(pizza_type, on_delete=models.CASCADE)
    pizza_size_id= models.ForeignKey(pizza_size, on_delete=models.CASCADE)
    status = models.ForeignKey(pizza_status, on_delete=models.CASCADE, default = 1)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.pizza_id)

class pizza_toppings(models.Model):
    pizza_toppings_id=models.AutoField(primary_key=True)
    toppings_id= models.ForeignKey(toppings, on_delete=models.CASCADE)
    pizza_id= models.ForeignKey(pizza, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.pizza_toppings_id)