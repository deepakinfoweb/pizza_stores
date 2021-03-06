"""
Python and predefine
"""
from rest_framework.views import APIView,Response
import datetime

"""
user path file 
"""
from pizza_info.models import pizza

class DeletePizza(APIView):
    def post(self,request,format='Json'):
        input_json = request.data
        output_json = {}
        output_json = delete_pizza(input_json)
        return Response(output_json)

def delete_pizza(input_json):
    output_json = {}
    try:
        if pizza.objects.filter(pizza_id = input_json['pizza_id'],status=1).exists():
            pizza.objects.filter( pizza_id= input_json['pizza_id']).update(status=2)
            output_json['Status'] = "Success" 
            output_json['Massage'] = "Pizza toppings has been deleted successfully."
        else:
            output_json['Status'] = "Failure" 
            output_json['Massage'] = "Pizza toppings has not been deleted successfully."
    except Exception as ex:
        output_json['Status'] = "Failure" 
        output_json['Massage'] = "Pizza toppings has not been deleted successfully.Excepation encountered is "+str(ex) 
    return output_json