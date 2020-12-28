"""
Python and predefine
"""
from rest_framework.views import APIView,Response
import datetime

"""
user path file 
"""
from pizza_info.models import pizza_toppings

class EditPizzaToppings(APIView):
    def post(self,request,format='Json'):
        input_json = request.data
        output_json = {}
        output_json = edit_pizza_toppings(input_json)
        return Response(output_json)

def edit_pizza_toppings(input_json):
    output_json = {}
    try:
        if pizza_toppings.objects.filter(pizza_toppings_id = input_json['pizza_toppings_id'],status=1).exists():
            pizza_toppings.objects.filter(pizza_toppings_id = input_json['pizza_toppings_id']).update(toppings=input_json['toppings'],last_modified_date=datetime.datetime.now())
            output_json['Status'] = "Success" 
            output_json['Massage'] = "Pizza toppings has been edited successfully."
        else:
            output_json['Status'] = "Failure" 
            output_json['Massage'] = "Pizza toppings has not been edited successfully."
    except Exception as ex:
        output_json['Status'] = "Failure" 
        output_json['Massage'] = "Pizza toppings has not been edited successfully.Excepation encountered is "+str(ex) 
    return output_json