from django.db import models
from datetime import datetime
def brand_logo_upload_path(instance, filename):
    return f'{instance.id}/{datetime.now().strftime("%Y%m%d")}_{filename}'
class BrandsDetails(models.Model):
    title = models.CharField(max_length=15)
    logo = models.FileField(upload_to=brand_logo_upload_path)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Brand_details'

class BrandUsers(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    brand = models.ForeignKey(BrandsDetails, on_delete=models.CASCADE)

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






