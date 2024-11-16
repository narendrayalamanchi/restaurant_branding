from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.gis.db import models as gis_models

def brand_logo_upload_path(instance, filename):
    return f'{instance.title}/{datetime.now().strftime("%Y%m%d")}_{filename}'

class BrandsDetails(models.Model):
    title = models.CharField(max_length=15,unique=True)
    logo = models.FileField(upload_to=brand_logo_upload_path)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Brand_details'

class BrandAddress(models.Model):
    brand = models.ForeignKey(BrandsDetails, related_name='addresses', on_delete=models.CASCADE)
    # building_number = models.CharField(max_length=50) # Apartment/ Suite / floor Numbers
    address = models.CharField(max_length=500)
    location = gis_models.PointField(geography=True, srid=4326, null=True) 

    def __str__(self):
        return f"{self.address}"

    class Meta:
        db_table = 'Brand_address'
        unique_together = ('brand', 'address')

class BrandUsers(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)
    brand = models.ForeignKey(BrandsDetails, on_delete=models.CASCADE)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Brand_users'

class MenuCategories(models.Model):
    brand = models.ForeignKey(BrandsDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    order = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Menu_categories'

def menuitem_image_upload_path(instance, filename):
    return f'{instance.category.brand}/{datetime.now().strftime("%Y%m%d")}_{filename}'

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    recipe_details = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.FileField(upload_to = menuitem_image_upload_path)
    order = models.IntegerField()
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Menu_items'






