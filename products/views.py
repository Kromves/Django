import datetime

from django.http import HttpResponse
from django.shortcuts import render

from products.models import Post


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello,World!')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def goodbay_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbay User')


def data_view(request):
    if request.method == 'GET':
        data = datetime.datetime.now()
        return HttpResponse(f'Current time is: {data}')


def post_list_view(request):
    posts = Post.objects.all()

    # 2. Передаем посты в контекст
    context = {'posts': posts}

    # 3. Отображаем шаблон
    return render(request, 'post_list.html', context)
