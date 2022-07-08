from django.urls import path

from .views import short_url,register,show_list,login

urlpatterns = [
    path('', short_url),
    path('register/', register),
    path('login/',login),
    path('urls_list/', show_list)

]