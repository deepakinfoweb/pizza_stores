""" python framework """
from django.shortcuts import render

""" user file path """
from pizza_info.serializers import pizza_type_Serializer
from pizza_info.models import pizza_type

"""
db connection 
"""
from django.db import transaction
from django.db import connection

def home(request):
    output_json = {}
    output_json['Payload'] = {}
    try:
        # import pdb; pdb.set_trace()
        type_query = """ select * from public.pizza_info_pizza_type where status_id = 1 order by name"""
        pizza_type = dbExecutionQuery(type_query)
        size_query = """ select * from public.pizza_info_pizza_size where status_id = 1 order by pizza_size_name """
        pizza_size = dbExecutionQuery(size_query)
        toppings_query = """ select * from public.pizza_info_pizza_toppings where status_id = 1 order by toppings"""
        pizza_toppings = dbExecutionQuery(toppings_query)
        output_json['Payload']['pizza_type'] = pizza_type
        output_json['Payload']['pizza_size'] = pizza_size
        output_json['Payload']['pizza_toppings'] = pizza_toppings
        output_json['Status'] = "Success" 
        output_json['Massage'] = "Pizza toppings has been edited successfully."
    except Exception as ex:
        output_json['Status'] = "Failure" 
        output_json['Massage'] = "Pizza toppings has not been edited successfully.Excepation encountered is "+str(ex) 
    return render(request,'index.html',output_json)

"""
db query execution
"""
def dbExecutionQuery(query):
    output_json ={}
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = dictfetchall(cursor)
        output_json = result
        return output_json
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "searchContent have not been fetched successfully. Exception encountered is " + str(ex)
        output_json['Payload'] = None
        return output_json

def dictfetchall(cursor):
    # "Return all rows from a cursor as a dict" 
    columns = [col[0] for col in cursor.description] 
    return [dict(zip(columns, row)) for row in cursor.fetchall()]