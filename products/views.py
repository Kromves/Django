import random
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello,World!')


def main_page_view(request):
    if request.method == 'GET':
        return render(request,'main.html' )

def goodbay_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbay User')

def data_view(request):
    if request.method == 'GET':
        data = datetime.datetime.now()
        return HttpResponse(f'Current time is: {data}')
