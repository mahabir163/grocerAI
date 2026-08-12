from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']  
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username or email already exists!! Try again.')
            return render(request, 'signup.html')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!! Try again.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('home')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')
