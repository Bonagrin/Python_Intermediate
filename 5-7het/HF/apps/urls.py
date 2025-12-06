from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    
    path('home/', views.home, name='home'),
    
    path('author/add/', views.add_author),
    path('author/add_record/', views.add_author_record),
    path('author/update/<int:id>', views.update_author),
    path('author/update/update_record/<int:id>', views.update_author_record),
    path('author/delete/<int:id>', views.delete_author),
    
    path('book/add/', views.add_book),
    path('book/add/add_record/', views.add_book_record),
    path('book/update/<int:id>', views.update_book),
    path('book/update/update_record/<int:id>', views.update_book_record),
    path('book/delete/<int:id>', views.delete_book),
]