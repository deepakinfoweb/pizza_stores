from rest_framework import serializers
from pizza_info.models import pizza_size,pizza_toppings,pizza_type

class pizza_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_type
        fields = '__all__'

class pizza_toppings_Serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_toppings
        fields = '__all__'

class pizza_size_Serializer(serializers.ModelSerializer):
    class Meta:
        model = pizza_size
        fields = '__all__'