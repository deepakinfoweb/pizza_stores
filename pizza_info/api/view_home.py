""" python framework """
from django.shortcuts import render

""" user file path """
from pizza_info.serializers import pizza_type_Serializer,PizzaSerializer
from pizza_info.models import pizza_type,pizza

"""
db connection 
"""
from django.db import transaction
from django.db import connection

def home(request):
    output_json = {}
    output_json['Payload'] = {}
    try:
        type_query = """ select * from public.pizza_info_pizza_type where status_id = 1 order by name"""
        pizza_type = dbExecutionQuery(type_query)
        size_query = """ select * from public.pizza_info_pizza_size where status_id = 1 order by pizza_size_name """
        pizza_size = dbExecutionQuery(size_query)
        toppings_query = """ select * from public.pizza_info_toppings where status_id = 1 order by toppings"""
        pizza_toppings = dbExecutionQuery(toppings_query)
        output_json['Payload']['pizza_type'] = pizza_type
        output_json['Payload']['pizza_size'] = pizza_size
        output_json['Payload']['pizza_toppings'] = pizza_toppings
        pizza_query = """select a.pizza_id,b.name,c.pizza_size_name from public.pizza_info_pizza a join public.pizza_info_pizza_type b on a.pizza_type_id_id =b.pizza_type_id join public.pizza_info_pizza_size c on a.pizza_size_id_id = c.pizza_size_id where a.status_id = 1 """
        pizza_qs = dbExecutionQuery(pizza_query)
        pizza_list = []
        for item in pizza_qs:
            pizza_item ={}
            pizza_item['pizza_id'] = item['pizza_id']
            pizza_item['name'] = item['name']
            pizza_item['pizza_size_name'] = item['pizza_size_name']
            toppings_query = """select b.toppings from public.pizza_info_pizza_toppings a join public.pizza_info_toppings b on a.toppings_id_id = b.toppings_id where a.pizza_id_id = """+str(item['pizza_id'])+""" """
            toppings_query_qs = dbExecutionQuery(toppings_query)
            topping_list =[]
            for itemj in toppings_query_qs:
                topping_list.append(itemj['toppings'])
            pizza_item['toppings'] =  topping_list
            pizza_list.append(pizza_item)
        output_json['Payload']['pizza'] = pizza_list
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