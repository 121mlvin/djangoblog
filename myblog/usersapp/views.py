from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main(request: HttpRequest):
    return HttpResponse('This is main page')


def about(request: HttpRequest):
    return HttpResponse('This is about page')


def profile_page(request: HttpRequest, username):
    return HttpResponse(f'This is your profile page page, {username}!')


def set_password(request: HttpRequest):
    return HttpResponse('This is set-password page')


def set_userdata(request: HttpRequest):
    return HttpResponse('This is set-userdata page')


def deactivate(request: HttpRequest):
    return HttpResponse('This is deactivate page')


def register(request: HttpRequest):
    return HttpResponse('This is register page')


def login(request: HttpRequest):
    return HttpResponse('This is login page')


def logout(request: HttpRequest):
    return HttpResponse('This is logout page')
