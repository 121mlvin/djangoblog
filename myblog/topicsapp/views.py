from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def topics(request: HttpRequest):
    return HttpResponse('This is topics page')


def topics_subscribe(request: HttpRequest, topic):
    return HttpResponse(f'Subscribed to topic: {topic}')


def topics_unsubscribe(request: HttpRequest, topic):
    return HttpResponse(f'Unsubscribe from topic: {topic}')
