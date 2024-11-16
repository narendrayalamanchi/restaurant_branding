from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.gis.db import models as gis_models
import admin_dashboard.models  as brand_models
from django.utils import timezone

class RestaurantUsers(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=10)
    brand = models.ForeignKey(brand_models.BrandsDetails, on_delete=models.CASCADE,default= None)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Restaurant_users'


class UserAddress(models.Model):
    user = models.ForeignKey(RestaurantUsers, on_delete=models.CASCADE, related_name='addresses')
    building_number = models.CharField(max_length=50, null=True) # Apartment/ Suite / floor Numbers
    address = models.CharField(max_length=500)
    location = gis_models.PointField(geography=True, srid=4326, null=True) 

    def __str__(self):
        return f"{self.address}"

    class Meta:
        db_table = 'User_address'
        unique_together = ('user', 'location')


class Cart(models.Model):
    user = models.ForeignKey(RestaurantUsers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.name} - Created on {self.created_at}"

    @property
    def total_items(self):
        # Returns the total number of items in the cart
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self):
        # Returns the total price of all items in the cart
        return round(sum(item.total_price for item in self.items.all()),2)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(brand_models.MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity}) in cart of {self.cart.user.name}"

    @property
    def total_price(self):
        # Returns the total price for this item based on its quantity
        return self.menu_item.price * self.quantity

    class Meta:
        unique_together = ('cart', 'menu_item')