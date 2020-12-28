# pizza_stores
1. first you clone the project.
2. activate your python environment
2. after clone you should run "python3 manage.py makemigrations pizza_info" and "python3 manage.py migrate"
3. after run above command you need to run "insert into public.pizza_info_pizza_status values(1,'active')" and "insert into public.pizza_info_pizza_status values(,'inactive')" in pgadmin
4.  after run above command you need to run "python3 manage.py runserver"

### API Documentation  ###
1. API for Create Pizza Type  
    url: http://127.0.0.1:8000/createPizzaType
    input_request : { "name" : "Regular" }
    response : {"Status": "Success", "Message": "Pizza type have been fetched successfully" }

2. API for Create Pizza Size 
    url: http://127.0.0.1:8000/createPizzaSize
    input_request : { "name" : "Small" }
    response : { "Status": "Success", "Message": "Pizza size have been fetched successfully" }

3. API for Create Pizza Toppings 
    url: http://127.0.0.1:8000/createPizzaToppings
    input_request : { "name" : "Corn" }
    response : { "Status": "Success", "Message": "Toppings have been fetched successfully" }

4. API for Edit Pizza Type  
    url: http://127.0.0.1:8000/editpizzatype
    input_request : { "pizza_type_id" : "1" }
    response : {"Status": "Success", "Message": "Pizza type has been edited successfully" }

5. API for Edit Pizza Size 
    url: http://127.0.0.1:8000/editpizzasize
    input_request : { "pizza_size_id" : "1" }
    response : { "Status": "Success", "Message": "Pizza size has been edited successfully" }

6. API for Edit Pizza Toppings 
    url: http://127.0.0.1:8000/editpizzatoppings
    input_request : { "pizza_toppings_id" : "1" }
    response : { "Status": "Success", "Message": "Pizza topping has been edited successfully" }

7. API for Delete Pizza Type  
    url: http://127.0.0.1:8000/deletepizzatype
    input_request : { "pizza_type_id" : "1" }
    response : {"Status": "Success", "Message": "Pizza type has been deleted successfully." }

8. API for Create Pizza Size 
    url: http://127.0.0.1:8000/deletepizzasize
    input_request : { "pizza_size_id" : "1" }
    response : { "Status": "Success", "Message": "Pizza size has been deleted successfully" }

9. API for Create Pizza Toppings 
    url: http://127.0.0.1:8000/deletepizzatoppings
    input_request : { "pizza_toppings_id" : "1" }
    response : { "Status": "Success", "Message": "Pizza topping has been deleted successfully" }
    

 
 
 
