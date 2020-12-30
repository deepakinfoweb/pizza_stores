"""
Python and django define package 
"""
from rest_framework.views import Response,APIView

"""
user define file and package 
"""
from pizza_info.serializers import pizza_type_Serializer
from pizza_info.models import pizza_type

class CreatePizzaTypeAPI(APIView):
    def post(self,request,format = 'Json'):
        input_json = request.data
        output_json = {}
        output_json = create_pizza_typeAPI(input_json)
        return Response(output_json)
"""
function for create api for pizza type
"""
def create_pizza_typeAPI(input_json):
    output_json ={}
    try:
        if pizza_type.objects.filter(name=input_json['name'],status = 1).exists() == False:
            insert_param = {}
            insert_param['name'] = input_json['name']
            try:
                serialized_pizza_params = pizza_type_Serializer(data = insert_param)
                if serialized_pizza_params.is_valid(raise_exception = True):
                    serialized_pizza_params.save()
                    output_json['Status'] = "Success"
                    output_json['Message'] = "Pizza type have been created successfully"
                else:
                    output_json['Status'] = "Failure"
                    output_json['Message'] = "Pizza type have not been created successfully"
            except Exception as ex:
                output_json['Status'] = "Failure"
                output_json['Message'] = "Pizza type have not been created successfully. Exception encountered is " + str(ex)
        else:
            output_json['Status'] = "Failure"
            output_json['Message'] = "Pizza type already exists in databse"
        return output_json
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "Pizza type have not been created successfully. Exception encountered is " + str(ex)
        output_json['Payload'] = None
        return output_json
