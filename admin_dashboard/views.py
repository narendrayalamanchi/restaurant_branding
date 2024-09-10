from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import BrandUsers, BrandsDetails, MenuCategories, MenuItem
from .forms import SignupForm,LoginForm, CategoryForm, MenuForm
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

# Create your views here.
def index(request):
    return render(request,'index.html')

def signout(request):
    logout(request)
    return render(request,'index.html')
                  
def signup(request):
    response = {"success": True}
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            response["message"] = "Invalid Details."
            response["success"] = False
    else:
        form = SignupForm()
        response["form"] = form

    return render(request,'brand_auth/register.html', response)

def login(request):
    response = {"success":True}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            users = BrandUsers.objects.filter(email=email, password = password)
            if users.exists():
                request.session["is_logged"] = True
                request.session["username"] = users[0].username
                request.session["brand"] = users[0].brand.id
                return redirect('dashboard')
            else:
                response["message"] = "Invalid Credentials/No User Found"
                response["success"] = False
    else:
        form = LoginForm
        response["form"] = form

    return render(request,'brand_auth/login.html', response)

def dashboard(request):
    cat = MenuCategories.objects.filter(brand=request.session["brand"])
    # print(cat)
    return render(request,'brand_dashboard/dashboard.html',{"categories": cat})

def create_category_form_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            brand_id = request.session["brand"]
            if brand_id:
                try:
                    brand = BrandsDetails.objects.get(id=brand_id)
                    category.brand = brand
                except BrandsDetails.DoesNotExist:
                    return redirect('error_page')

            category.save()
            return JsonResponse({'success': True,'category': {'id':category.id,'name':category.name,'order':category.order} })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    form = CategoryForm()
    return render(request, 'brand_dashboard/popups/create_category.html', {'form': form})

def create_menu_form_view(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            print(form.errors)
            return JsonResponse({'success': False, 'errors': form.errors})

    form = MenuForm()
    return render(request, 'brand_dashboard/popups/create_menuitem.html', {'form': form})


def category(request):
    cat = MenuCategories.objects.filter(brand=request.session["brand"]).order_by('order')
    return render(request, 'brand_dashboard/category.html', {"categories": cat})

@csrf_exempt
def update_category_order(request):
    data = json.loads(request.body)
    dragged_id = data.get('dragged_id')
    dragged_order = data.get('dragged_order')
    drop_id = data.get('drop_id')
    drop_order = data.get('drop_order')
    try:
        MenuCategories.objects.filter(id=dragged_id).update(order= drop_order)
        MenuCategories.objects.filter(id=drop_id).update(order= dragged_order)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def menu(request):
    menu_items = MenuItem.objects.filter(category__brand=request.session["brand"]).order_by('category__order','order')
    print(menu_items)
    return render(request, "brand_dashboard/menu.html", {"menu": menu_items})