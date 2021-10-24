import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import InstaForm
from .models import UsernameInstagramUser
from .script import insta_load

# Create your views here.

def index(request):

    form = InstaForm()
    if request.method == 'POST':
        form = InstaForm(request.POST)
        if form.is_valid():
            if not (UsernameInstagramUser.objects.filter(username=form.cleaned_data['username']).exists()):
                form.save()

            user = insta_load.InstaloaderUser(form.cleaned_data['username'])

            private = user.get_privated()
            if private:
                print("privated")
                context = {'form': form, 'private': 'private'}
                return render(request, 'insta_app/index.html', context)

            else:
                print("not private")
                data = user.get_data_profile()
                context = {'form': form, 'result': data}
                return render(request, 'insta_app/index.html', context)

    context = {'form': form}
    return render(request, 'insta_app/index.html', context)

