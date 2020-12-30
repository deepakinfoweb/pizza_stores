"""
Python and django define package 
"""
from rest_framework.views import Response,APIView

"""
user define file and package 
"""
from pizza_info.serializers import PizzaSerializer,pizzaToppingsSerializer
from pizza_info.models import pizza,pizza_toppings

class CreatePizzaAPI(APIView):
    def post(self,request,format = 'Json'):
        input_json = request.data
        output_json = {}
        output_json = create_pizza_API(input_json)
        return Response(output_json)
"""
function for create api for pizza
"""
def create_pizza_API(input_json):
    output_json ={}
    try:
        insert_param = {}
        insert_param['pizza_type_id'] = input_json['pizza_type_id']
        insert_param['pizza_size_id'] = input_json['pizza_size_id']
        try:
            serialized_pizza_params = PizzaSerializer(data = insert_param)
            if serialized_pizza_params.is_valid(raise_exception = True):
                serialized_pizza_params.save()
                pizza_id_var = serialized_pizza_params.data['pizza_id']
                for item in input_json['toppings_list']:
                    insertion_param = {}
                    insertion_param['toppings_id'] = item
                    insertion_param['pizza_id'] = pizza_id_var
                    try:
                        serialized_pizza_toppings_params = pizzaToppingsSerializer(data = insertion_param)
                        if serialized_pizza_toppings_params.is_valid(raise_exception = True):
                            serialized_pizza_toppings_params.save()
                    except Exception as ex:
                        output_json['Status'] = "Failure"
                        output_json['Message'] = "Pizza have not been created successfully. Exception encountered is " + str(ex)
                output_json['Status'] = "Success"
                output_json['Message'] = "Pizza have been created successfully"
            else:
                output_json['Status'] = "Failure"
                output_json['Message'] = "Pizza have not been created successfully"
        except Exception as ex:
            output_json['Status'] = "Failure"
            output_json['Message'] = "Pizza have not been created successfully. Exception encountered is " + str(ex)
        return output_json
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "Pizza have not been created successfully. Exception encountered is " + str(ex)
        output_json['Payload'] = None
        return output_json
