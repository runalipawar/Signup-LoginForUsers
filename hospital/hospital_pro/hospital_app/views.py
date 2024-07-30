from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm 

def index(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(f'User created: {user.username}, Redirecting...')
            if user.is_patient:
                print('Redirecting to patient dashboard...')
                return redirect('patient_dashboard')
            elif user.is_doctor:
                print('Redirecting to doctor dashboard...')
                return redirect('doctor_dashboard')
            else:
                print('User is neither patient nor doctor.')
        else:
            print('Form is not valid:', form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'index.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f'User logged in: {user.username}, Redirecting...')
            if user.is_patient:
                print('Redirecting to patient dashboard...')
                return redirect('patient_dashboard')
            elif user.is_doctor:
                print('Redirecting to doctor dashboard...')
                return redirect('doctor_dashboard')
            else:
                print('User is neither patient nor doctor.')
        else:
            print('Login form is not valid:', form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
