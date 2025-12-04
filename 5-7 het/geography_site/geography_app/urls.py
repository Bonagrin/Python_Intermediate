from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/add/', views.add_country),
    path('country/add_record/', views.add_country_record),
    path('country/update/<int:id>', views.update_country),
    path('country/update/update_record/<int:id>', views.update_country_record),
    path('country/delete/<int:id>', views.delete_country),
    path('city/add/', views.add_city),
    path('city/add/add_record/', views.add_city_record),
    path('city/update/<int:id>', views.update_city),
    path('city/update/update_record/<int:id>', views.update_city_record),
    path('city/delete/<int:id>', views.delete_city),
]
