"""
Python and predefine
"""
from rest_framework.views import APIView,Response
import datetime

"""
user path file 
"""
from pizza_info.models import pizza
from pizza_info.api.Create_API.create_pizza_API import create_pizza_API

class EditPizza(APIView):
    def post(self,request,format='Json'):
        input_json = request.data
        output_json = {}
        output_json = edit_pizza(input_json)
        return Response(output_json)

def edit_pizza(input_json):
    output_json = {}
    try:
        if pizza.objects.filter(pizza_id = input_json['pizza_id'],status=1).exists():
            pizza.objects.filter(pizza_id = input_json['pizza_id']).update(status=2)
            create_pizza_API(input_json)
            output_json['Status'] = "Success" 
            output_json['Massage'] = "Pizza has been edited successfully."
        else:
            output_json['Status'] = "Failure" 
            output_json['Massage'] = "Pizza has not been edited successfully."
    except Exception as ex:
        output_json['Status'] = "Failure" 
        output_json['Massage'] = "Pizza has not been edited successfully.Excepation encountered is "+str(ex) 
    return output_json