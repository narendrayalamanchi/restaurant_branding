from django.urls import path
from . import views,cart

urlpatterns = [
    path('', views.home_page, name='res_home'),
    path('login/', views.login, name='res_login'),
    path('signup/', views.signup, name='res_signup'),
    path('signout/', views.signout, name='res_signout'),
    path('dashboard/', views.dashboard, name='res_dashboard'),
    path('findnearybylocations/', views.findnearybylocations, name='find-nearby-restaurant-locations'),

    # Cart Logic
    path('cartview/', cart.view_cart, name='view_cart'),
    path('cart/additems/', cart.add_to_cart, name='add_to_cart'),
    path('cart/removeitems/', cart.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', cart.clear_cart_view, name='clear_cart_view'),
]