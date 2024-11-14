
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from admin_dashboard.models import MenuItem
from .models import RestaurantUsers,Cart,CartItem
import json
from .views import load_custom_user

@load_custom_user
def add_to_cart(request):
    try:
        data = json.loads(request.body)
        item_id =  data.get('item_id')
        menu_item = get_object_or_404(MenuItem, id=item_id)
        cart = get_user_cart(request.user)
        upd_quantity = add_item_to_cart(cart, menu_item.id, quantity=1)

        return JsonResponse({"status":"success","quantity":upd_quantity})
    except MenuItem.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Menu item not found"}, status=404)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@load_custom_user
def view_cart(request):
    cart = get_user_cart(request.user)
    return JsonResponse({"status":"success",'cart': cart})

@load_custom_user
def remove_from_cart(request):
    data = json.loads(request.body)
    item_id =  data.get('item_id')
    type =  data.get('type')
    cart = get_user_cart(request.user)
    if type == "remove":
        remove_item_from_cart(cart, item_id)
    else:
        change_itemquantity_to_cart(cart, item_id, quantity=1)
    
    return JsonResponse({"status":"success",'type': type})

@load_custom_user
def clear_cart_view(request):
    cart = get_user_cart(request.user)
    clear_cart(cart)
    return JsonResponse({"status":"success"})

# Cart utils functions
def get_user_cart(user):
    # Retrieve existing cart or create a new one for the user
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

def add_item_to_cart(cart, menu_item_id, quantity=1):
    # Add item to cart or increase quantity if it exists
    item, created = CartItem.objects.get_or_create(cart=cart, menu_item_id=menu_item_id)
    if not created:
        item.quantity += quantity
    item.save()
    return item.quantity

def change_itemquantity_to_cart(cart, menu_item_id, quantity=1):
    # Reduce item quantity in the cart 
    item = CartItem.objects.get(cart=cart, menu_item_id=menu_item_id)
    item.quantity -= quantity
    item.save()

def remove_item_from_cart(cart, menu_item_id):
    # Remove item from the cart
    CartItem.objects.filter(cart=cart, menu_item_id=menu_item_id).delete()

def clear_cart(cart):
    # Clear all items in the cart
    cart.items.all().delete()