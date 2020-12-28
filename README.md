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
 
 
