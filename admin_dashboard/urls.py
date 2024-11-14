from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.brand_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('category/', views.category, name='category'),
    path('menu/', views.menu, name='menu'),
    path('locations/', views.locations, name='locations'),
    path('addbrandaddress/', views.addbrandaddress, name='addbrandaddress'),
    path('deletebrandaddress/', views.deletebrandaddress, name='deletebrandaddress'),

    #POPUP FORMS API's
    path('category-form/', views.create_category_form_view, name='category-form'),
    path('menu-form/', views.create_menu_form_view, name='menu-form'),

    #Update Orders 
    path('update-category-order/', views.update_category_order, name='update-category-order'),
]
