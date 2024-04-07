from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . models import Car, CarImage, CarDocument, CarExpense

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone Number')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']  # Change 'password' to 'password2'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user


class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']

class CarDocumentForm(forms.ModelForm):
    class Meta:
        model = CarDocument
        fields = ['name', 'document']

class CarExpenseForm(forms.ModelForm):
    class Meta:
        model = CarExpense
        fields = ['name', 'price']

CarImageFormSet = forms.inlineformset_factory(Car, CarImage, form=CarImageForm, extra=4)
CarDocumentFormSet = forms.inlineformset_factory(Car, CarDocument, form=CarDocumentForm, extra=4)
CarExpenseFormSet = forms.inlineformset_factory(Car, CarExpense, form=CarExpenseForm, extra=4)

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        