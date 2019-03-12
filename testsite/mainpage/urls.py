from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.Employee.as_view(), name = 'employee'),
    path('person/<pk>/', views.Person.as_view(), name = 'person'),
    path('search/', views.Search.as_view(), name = 'search'),
    path('pass_logout/', views.passlogout, name='pass_logout'),
    path('', views.Loginpage.as_view(), name='loginpage'),
    path('register/', views.Registerpage.as_view(), name='registerpage'),
    path('edit/<pk>/', views.Editperson.as_view(), name='editperson'),
    path('create/', views.Createperson.as_view(), name='createperson'),
]
