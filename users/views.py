from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import RegisterForm
from django.contrib import messages
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import requests
import json


API_KEY = '194dc2affe7d420aa7228b2a6e311f5d'
API_URL = 'https://emailvalidation.abstractapi.com/v1/?api_key=' + API_KEY

# Class Based Views
class RegisterView(CreateView, FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login-user') 
    def get_success_url(self):
        return self.success_url

# Function / Function based views
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home-url')
        else:
            messages.warning(request, 'Please Check Username or Password')

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('home-url')
            
def add_friend_view(request, profile_id):
    user = Profile.objects.get(pk=request.user.profile.id)
    friend = Profile.objects.get(pk=profile_id)
    user.add_friend(profile2)
    return HttpResponse("Friend added successfully")




    
    return render(request, 'users/login.html')

def valid(email):
    response = requests.get(API_URL + "&email=" + email)
    response_content = response.content 
    data = json.loads(response_content.decode('utf-8'))
    print(data['is_smtp_valid']['value'])

    return data['is_smtp_valid']['value']
    


    

