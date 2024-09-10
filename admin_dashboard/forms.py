from django import forms 
from .models import BrandUsers, BrandsDetails, MenuCategories, MenuItem

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username_validate', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email_validate', 'placeholder': 'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    brand_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'brandtitle_validate', 'placeholder': 'Enter Brand Title'}))
    brand_logo = forms.FileField(widget=forms.FileInput())

    class Meta:
        model = BrandUsers
        fields = ['username', 'email', 'password','brand_title','brand_logo']
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        brand_title = self.cleaned_data.get('brand_title')
        brand_logo = self.cleaned_data.get('brand_logo')
        brand = BrandsDetails.objects.create(
            title = brand_title,
            logo = brand_logo
        )
        user.brand = brand
        if commit:
            user.save()

        return user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email_validate', 'placeholder': 'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

class CategoryForm(forms.ModelForm):

    class Meta:
        model = MenuCategories
        fields = ['name', 'order']

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['category', 'name', 'recipe_details','price','image','order']