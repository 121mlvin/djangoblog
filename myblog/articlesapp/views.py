from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def article(request: HttpRequest, article):
    return HttpResponse(f'This is {article} article')


def article_comment(request: HttpRequest, article):
    return HttpResponse(f'This is comment to this {article} article')


def article_update(request: HttpRequest, article):
    return HttpResponse(f'{article} updated')


def article_delete(request: HttpRequest, article):
    return HttpResponse(f'{article} deleted')


def create(request: HttpRequest):
    return HttpResponse('This is create page')
