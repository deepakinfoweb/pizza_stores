from rest_framework import serializers
from pizza_info.models import pizza_size,toppings,pizza_type,pizza,pizza_toppings

class pizza_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_type
        fields = '__all__'

class toppings_Serializer(serializers.ModelSerializer):
    class Meta:
        model = toppings
        fields = '__all__'

class pizza_size_Serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_size
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta :
        model = pizza
        fields = '__all__'


class pizzaToppingsSerializer(serializers.ModelSerializer):
    class Meta :
        model = pizza_toppings
        fields = '__all__'