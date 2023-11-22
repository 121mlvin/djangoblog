from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main(request: HttpRequest):
    return render(request, 'index.html')


def about(request: HttpRequest):
    return render(request, 'about.html')


def profile_page(request: HttpRequest, username):
    return HttpResponse(f'This is your profile page page, {username}!')


def set_password(request: HttpRequest):
    return HttpResponse('This is set-password page')


def set_userdata(request: HttpRequest):
    return HttpResponse('This is set-userdata page')


def deactivate(request: HttpRequest):
    return HttpResponse('This is deactivate page')


def register(request: HttpRequest):
    return render(request, 'register.html')


def login(request: HttpRequest):
    return render(request, 'login.html')


def logout(request: HttpRequest):
    return HttpResponse('This is logout page')
