import json

from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from user_auth.forms import UserLoginForm, UserRegistrationForm
from user_auth.models import UserInput
from user_auth.serializers import UserSerializer, SearchSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

def index(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('Login')
    return render(request, template_name='user_auth/index.html')


def login_attempt(request):
    _next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('Index')
    if request.method == 'POST':
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            if _next:
                return redirect(_next)
            return redirect('Index')
        return render(request, 'user_auth/login.html', {'form': form})
    return render(request, 'user_auth/login.html', {'form': form})


def logout_attempt(request):
    logout(request)
    return redirect('Login')


def register_attempt(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Login')
        return render(request, 'user_auth/register.html', {'form': form})
    return render(request, 'user_auth/register.html', {'form': form})


def saveInput(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data['input'])
        userinput = UserInput(input=data['input'], user=request.user)
        userinput.save()
        return JsonResponse({'message': "success"})
    return JsonResponse({'message': "error"})


class UserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserInputApi(viewsets.ModelViewSet):
    queryset = UserInput.objects.all()
    serializer_class = SearchSerializer

