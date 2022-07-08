from django.contrib import messages
from django.shortcuts import render
import pyshorteners
from django.core.validators import URLValidator
from .forms import UrlShortForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import URL


def short_url(request):
    form = UrlShortForm
    tiny_url = ""
    url_long = ""
    if 'submit' in request.POST:
        url_long = request.POST.get('url_long')

    validate_url = URLValidator()

    try:
        validate_url(url_long)
        s = pyshorteners.Shortener()
        tiny_url = str(s.tinyurl.short(url_long))
        URL.objects.create(url_long=url_long, url_short=tiny_url, user=request.user)

    except:
        tiny_url = ""

    context = {
            'form': form,
            'url': tiny_url
        }

    return render(request,template_name='urlshort_app/index.html',context=context)


def register(request):
    context = {}
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        messages.success(request, 'Account created successfully')
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, template_name='urlshort_app/register.html', context=context)

def login(request):
    context = {}
    if request.POST == 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm()
        context = {
            'form': form
        }
    return render(request, template_name='urlshort_app/login.html', context=context)

def show_list(request):
    urls = URL.objects.filter(user=request.user).values()

    context = {
        'urls':urls
    }
    return render(request=request,template_name='urlshort_app/list.html',context=context)


