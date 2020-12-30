"""
Python and django define package 
"""
from rest_framework.views import Response,APIView

"""
user define file and package 
"""
from pizza_info.serializers import toppings_Serializer
from pizza_info.models import toppings

class CreatePizzaToppingsAPI(APIView):
    def post(self,request,format = 'Json'):
        input_json = request.data
        output_json = {}
        output_json = create_pizza_toppings_API(input_json)
        return Response(output_json)
"""
function for create api for pizza type
"""
def create_pizza_toppings_API(input_json):
    output_json ={}
    try:
        if toppings.objects.filter(toppings=input_json['toppings'],status=1).exists() == False:
            insert_param = {}
            insert_param['toppings'] = input_json['toppings']
            try:
                serialized_pizza_params = toppings_Serializer(data = insert_param)
                if serialized_pizza_params.is_valid(raise_exception = True):
                    serialized_pizza_params.save()
                    output_json['Status'] = "Success"
                    output_json['Message'] = "Toppings have been created successfully"
                else:
                    output_json['Status'] = "Failure"
                    output_json['Message'] = "Toppings have not been created successfully"
            except Exception as ex:
                output_json['Status'] = "Failure"
                output_json['Message'] = "Toppings have not been created successfully. Exception encountered is " + str(ex)
        else:
            output_json['Status'] = "Failure"
            output_json['Message'] = "Toppings already exists in databse"
        return output_json
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "Toppings have not been created successfully. Exception encountered is " + str(ex)
        output_json['Payload'] = None
        return output_json
