from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm, LoginForm
from .models import BorrowCar, RentCar, Content, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def index(request):
    return render(request, 'index.html')

def car(request):
    BorrowCarstable = BorrowCar.objects.all()
    return render(request, 'car.html', locals())


def car_single(request):
    BorrowCar_Car_Id = request.GET['Car_Id']
    BorrowCar_Id = BorrowCar.objects.filter(Car_Id=BorrowCar_Car_Id)

    if request.method == "POST":
        rent = RentCar()
        rent.username = request.POST.get('username')
        rent.phone = request.POST.get('phone')
        rent.email = request.POST.get('email')
        rent.pickup_location = request.POST.get('pickup_location')
        rent.dropoff_location = request.POST.get('dropoff_location')
        rent.pickup_date = request.POST.get('pickup_date')
        rent.dropoff_date = request.POST.get('dropoff_date')
        rent.pickup_time = request.POST.get('pickup_time')
        rent.remarks = request.POST.get('remarks')
        rent.rent_number = request.POST.get('rent_number')
        rent.save()
        messages.success(request, "Rent Car Successfully!!!")
        return redirect('/')


    return render(request, 'car-single.html', locals())


def contact(request):
    if request.method == "POST":
        con = Content()
        con.username = request.POST.get('username')
        con.email = request.POST.get('email')
        con.subject = request.POST.get('subject')
        con.message = request.POST.get('message')
        con.message_created_time = request.POST.get('message_created_time')
        con.save()
        messages.success(request, "Message Send Successfully!!!")
        return redirect('/')
    return render(request, 'contact.html')


def trainmodel(request):
    return render(request, 'trainmodel.html')

@login_required(login_url="Login")
def borrowcarrecord(request):
    BorrowCar_username = request.GET['username']
    BorrowCars = BorrowCar.objects.filter(username=BorrowCar_username)
    return render(request, 'borrowcarrecord.html', locals())

@login_required(login_url="Login")
def rentcarrecord(request):
    RentCar_username = request.GET['username']
    RentCars = RentCar.objects.filter(username=RentCar_username)
    return render(request, 'rentcarrecord.html', locals())

@login_required(login_url="Login")
def addcar(request):
    if request.method == "POST":
        prod = BorrowCar()
        prod.username = request.POST.get('username')
        prod.email = request.POST.get('email')
        prod.Car_Id = request.POST.get('Car_Id')
        prod.Car_Name = request.POST.get('Car_Name')
        prod.Car_Description = request.POST.get('Car_Description')
        prod.Car_Rental_Price = request.POST.get('Car_Rental_Price')
        prod.Car_borrow_created = request.POST.get('Car_borrow_created')
        prod.CarImage = request.FILES['CarImage']
        prod.save()
        messages.success(request, "Car Added Successfully!!!")
        return redirect('/')
    return render(request, 'addcar.html')

@csrf_exempt
@csrf_protect
def login(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    context = {'form': form}
    return render(request.POST.get('next'), 'login.html', context or 'where_ever_you_send_your_user')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/login/')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url="Login")
def logout(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url="Login")
def profile(request):
    return render(request, 'profile.html', locals())


