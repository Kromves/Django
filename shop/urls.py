from django.contrib import admin
from django.urls import path

from products.views import hello_view, post_list_view
from products.views import main_page_view, goodbay_view, data_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view),
    path('hello/', hello_view),
    path('Goodbay/', goodbay_view),
    path('data/', data_view),
    path('posts/', post_list_view, name='post_list')

]
