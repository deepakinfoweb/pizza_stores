"""pizza_stores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

"""
user define file paths
"""
#--create API --start-#
from pizza_info.api.Create_API.create_pizza_type_API import CreatePizzaTypeAPI
from pizza_info.api.Create_API.create_pizza_size_API import CreatePizzaSizeAPI
from pizza_info.api.Create_API.create_pizza_toppings_API import CreatePizzaToppingsAPI
from pizza_info.api.Create_API.create_pizza_API import CreatePizzaAPI
#--create API --End-#

#--Edit API --start-#
from pizza_info.api.Edit_API.edit_pizza_type_API import EditPizzaType
from pizza_info.api.Edit_API.edit_pizza_size_API import EditPizzaSize
from pizza_info.api.Edit_API.edit_pizza_toppings_API import EditPizzaToppings
from pizza_info.api.Edit_API.edit_pizza_API import EditPizza
#--Edit API --end --#

#---Delete API-- start--#
from pizza_info.api.Delete_API.delete_pizza_type_API import DeletePizzaType
from pizza_info.api.Delete_API.delete_pizza_size_API import DeletePizzaSize
from pizza_info.api.Delete_API.delete_pizza_topping_API import DeletePizzaToppings
from pizza_info.api.Delete_API.delete_pizza_API import DeletePizza
#---Delete API-- end--#
from pizza_info.api.view_home import home

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$',home, name=''),

    #----------Pizza store API start------------------#
    
    #--create API --start-#
    url(r'^createPizzaType$', CreatePizzaTypeAPI.as_view(), name='createPizzaType'),
    url(r'^createPizzaSize$', CreatePizzaSizeAPI.as_view(), name='createPizzaSize'),
    url(r'^createPizzaToppings$', CreatePizzaToppingsAPI.as_view(), name='createPizzaToppings'),
    url(r'^createPizza$', CreatePizzaAPI.as_view(), name='createPizza'),
    #--create API --end-#

    #---edit API-- start--#
    url(r'^editpizzatype$', EditPizzaType.as_view(), name='editpizzatype'),
    url(r'^editpizzasize$', EditPizzaSize.as_view(), name='editpizzasize'),
    url(r'^editpizzatoppings$', EditPizzaToppings.as_view(), name='editpizzatoppings'),
    url(r'^editpizza$', EditPizza.as_view(), name='editpizza'),
    #---edit API-- end--#

    #---Delete API-- start--#
    url(r'^deletepizzatype$', DeletePizzaType.as_view(), name='deletepizzatype'),
    url(r'^deletepizzasize$', DeletePizzaSize.as_view(), name='deletepizzasize'),
    url(r'^deletepizzatoppings$', DeletePizzaToppings.as_view(), name='deletepizzatoppings'),
    url(r'^deletepizza$', DeletePizza.as_view(), name='deletepizza'),
    #--Delete API-- end--#

    #----------Pizza store API end ------------------#
]
