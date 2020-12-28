"""
Python and django define package 
"""
from rest_framework.views import Response,APIView

"""
user define file and package 
"""
from pizza_info.serializers import pizza_size_Serializer
from pizza_info.models import pizza_size

class CreatePizzaSizeAPI(APIView):
    def post(self,request,format = 'Json'):
        input_json = request.data
        output_json = {}
        output_json = create_pizza_size_API(input_json)
        return Response(output_json)
"""
function for create api for pizza type
"""
def create_pizza_size_API(input_json):
    output_json ={}
    try:
        if pizza_size.objects.filter(pizza_size_name=input_json['name'],status=1).exists() == False:
            insert_param = {}
            insert_param['pizza_size_name'] = input_json['name']
            try:
                serialized_pizza_params = pizza_size_Serializer(data = insert_param)
                if serialized_pizza_params.is_valid(raise_exception = True):
                    serialized_pizza_params.save()
                    output_json['Status'] = "Success"
                    output_json['Message'] = "Pizza size have been fetched successfully"
                else:
                    output_json['Status'] = "Failure"
                    output_json['Message'] = "Pizza size have not been fetched successfully"
            except Exception as ex:
                output_json['Status'] = "Failure"
                output_json['Message'] = "Pizza size have not been fetched successfully. Exception encountered is " + str(ex)
        else:
            output_json['Status'] = "Failure"
            output_json['Message'] = "Pizza size already exists in databse"
        return output_json
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "Pizza size have not been fetched successfully. Exception encountered is " + str(ex)
        output_json['Payload'] = None
        return output_json
