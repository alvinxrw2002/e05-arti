import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Karya
from .forms import FormKarya
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def index(request):
    loggedin_user = request.user
    objects = Karya.objects.all()
    context = {
        'user' : loggedin_user,
        'karyas' : objects
    }
    return render(request, 'index.html', context)

def login_user(request):
    if request.user:
        logout_user(request)

    if request.method == 'POST':
        # Autentikasikan username dan password
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("arti:index")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('arti:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/login')
def logout_user(request):
    # Redirect ke halaman login dan hapus cookie
    logout(request)
    response = HttpResponseRedirect(reverse('arti:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def post_karya(request):
    if request.method == 'POST':
        form = FormKarya(request.POST, request.FILES)
        if form.is_valid():
            karya = form.save(commit=False)
            karya.user = request.user
            karya.save()
            return redirect('arti:index')

    # jika method-nya GET atau yang lainnya, buat form kosong
    else:
        form = FormKarya()

    # Tampilkan form baru
    return render(request, 'post-karya.html', {'form': form})

# @login_required(login_url='/login')
# @csrf_exempt
# def add(request):
#     if request.method == 'POST':
#         form = FormKarya(request.POST, request.FILES)
#         if form.is_valid():
#             karya = form.save(commit=False)
#             karya.user = request.user
#             karya.save()
#             return HttpResponse("success")