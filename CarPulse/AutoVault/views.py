from django.shortcuts import render, redirect, get_object_or_404
from . models import Car
from . forms import CarDocumentFormSet, CarExpenseFormSet, CarForm, CarImageFormSet
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-list')  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        logout(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next', 'car-list'))  # Redirect to 'products' or your desired URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def add_car(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        image_formset = CarImageFormSet(request.POST, request.FILES, instance=Car())
        document_formset = CarDocumentFormSet(request.POST, request.FILES, instance=Car())
        expense_formset = CarExpenseFormSet(request.POST, request.FILES, instance=Car())
        if car_form.is_valid() and image_formset.is_valid() and document_formset.is_valid() and expense_formset.is_valid():
            car_instance = car_form.save()
            image_formset.instance = car_instance
            image_formset.save()
            document_formset.instance = car_instance
            document_formset.save()
            expense_formset.instance = car_instance
            expense_formset.save()
            return redirect('car-list')
    else:
        car_form = CarForm()
        image_formset = CarImageFormSet(instance=Car())
        document_formset = CarDocumentFormSet(instance=Car())
        expense_formset = CarExpenseFormSet(instance=Car())
    return render(request, 'add_car.html', {'car_form': car_form, 'image_formset': image_formset, 'document_formset': document_formset, 'expense_formset': expense_formset})



def list_cars(request):
    cars = Car.objects.all()
    return render(request, 'list_cars.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    total_expenses = sum(expense.price for expense in car.expenses.all())
    total_price = car.buying_price + total_expenses - car.discount

    context = {
        'car': car,
        'total_expenses': total_expenses,
        'total_price': total_price
    }
    return render(request, 'car_detail.html', context)


def update_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES, instance=car)
        if car_form.is_valid():
            car_form.save()
            return redirect('car-list')  # Redirect to the list view after updating
    else:
        car_form = CarForm(instance=car)
    return render(request, 'update_car.html', {'car_form': car_form, 'car': car})  # Pass the car instance to the template context


def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('car-list')
    return render(request, 'delete_car.html', {'car': car})
