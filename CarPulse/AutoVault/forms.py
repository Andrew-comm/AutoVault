from django import forms

from . models import Car, CarImage, CarDocument, CarExpense


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

        