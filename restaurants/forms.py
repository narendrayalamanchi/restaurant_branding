from django import forms 
from .models import RestaurantUsers
import admin_dashboard.models  as brand_models

class SignupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name_validate', 'placeholder': 'Enter Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email_validate', 'placeholder': 'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'phonenumber_validate', 'placeholder': 'Enter Phone Number'}))
    brandname = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = RestaurantUsers
        fields = ['name', 'email', 'password','phone_number']
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        brand_instance = brand_models.BrandsDetails.objects.filter(title=self.cleaned_data['brandname']).first()
        user.brand = brand_instance
      
        if commit:
            user.save()

        return user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email_validate', 'placeholder': 'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))