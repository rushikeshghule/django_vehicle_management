from django.shortcuts import render, redirect,get_object_or_404
from .forms import SignUpForm, LoginForm ,VehicleForm
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse
from .models import Vehicle
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout


def index(request):
    return render(request, 'vehicles/index.html')


def register(request):
    msg = 'Enter details'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created successfully now you can login'

        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'vehicles/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_user:
                login(request, user)
                return redirect('vehicle_list')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('vehicle_list')
            elif user is not None and user.is_superadmin:
                login(request, user)
                return redirect('vehicle_list')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'vehicles/login.html', {'form': form, 'msg': msg})

def logout_view(request):
    logout(request)
    return redirect('login_view')







@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

@login_required
@user_passes_test(lambda u: u.is_superadmin or u.is_admin, login_url='/unauthorized/')
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/vehicle_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superadmin or u.is_admin, login_url='/unauthorized/')
def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            vehicle = form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/vehicle_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superadmin, login_url='/unauthorized/')
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_confirm_delete.html', {'vehicle': vehicle})

def unauthorized(request):
    return render(request, 'vehicles/unauthorized.html')


