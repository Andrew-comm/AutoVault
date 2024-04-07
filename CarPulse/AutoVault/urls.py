
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_car', views.add_car, name='add-car'),
    path('car_list', views.list_cars, name='car-list'),
    path('car_detail/<int:car_id>', views.car_detail, name='car-detail'),
    path('update_car/<int:car_id>', views.update_car, name='update-car'),
    path('delete_car/<int:car_id>', views.delete_car, name='delete-car'),

    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
   
]
