from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from book.models import Book
from main.models import Profile
from main.forms import RegisterForm, LoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
def show_main(request):
    return render(request, "main.html")

def show_home(request):
    return render(request, "home.html")
@csrf_exempt
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(
                user = new_user,
                role = new_user.role,
                name = new_user.name,
                bio_data = new_user.bio_data,
                preferred_genre = new_user.preferred_genre,
            )
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {'form':form}
    return render(request, 'login.html', context)

@csrf_protect
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

@login_required
def profile_user(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        
        role = request.POST.get('role')
        name = request.POST.get('name')
        bio_data = request.POST.get('bio_data')
        preferred_genre = request.POST.get('preferred_genre')
        
        if not name:
            messages.error(request, 'Name is required.')
            return redirect('main:update_profile')

        profile.role = role
        profile.name = name
        profile.bio_data = bio_data
        profile.preferred_genre = preferred_genre
        profile.save()
        
        messages.success(request, 'Your profile was successfully updated!')
        return redirect('main:profile_user')
    else:
        messages.error(request, 'Invalid request')
        return redirect('main:profile_user')


def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")