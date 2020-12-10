from django.shortcuts import render, redirect
from . import models
from django.http import Http404
from django.http import HttpResponse
import pdb
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.

from .forms import CreateUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def room(request):
    ro = models.rooms.objects.all()
    return render(request, "room.html", {"ro": ro})


@login_required(login_url='login')
def search(request):
    ro = models.rooms.objects.all()
    val1 = request.POST['num1']
    return render(request, "search.html", {"ro": ro, "val1": val1})


@login_required(login_url='login')
def book(request, obj_id):
    request.session['val700'] = obj_id
    return render(request, "booking.html")


@login_required(login_url='login')
def confirm(request):
    val8 = int(request.POST['adult'])
    val10 = int(request.POST['child'])
    val11 = int(request.POST['nights'])

    cost = (val11 * ((val8 * 1000) + (val10 * 500)))
    request.session['val12'] = request.POST['name']
    request.session['val2'] = request.POST['adult']
    request.session['val3'] = request.POST['child']
    request.session['val13'] = request.POST['no']
    request.session['val9'] = request.POST['room_code']
    request.session['val6'] = request.POST['nights']
    request.session['val30'] = request.POST['checkin']
    request.session['var'] = cost
    request.session['val150'] = request.POST['email']
    return render(request, "confirm.html", {'cost': cost})


@login_required(login_url='login')
def payment(request):
    if 'val700' not in request.session:
        return redirect('/')
    cost = request.session['val700']
    return render(request, "Payment.html", {'cost': cost})


@login_required(login_url='login')
def success(request):

    guest1 = models.guest()
    guest1.Head_name = request.session['val12']
    guest1.No_of_adults = request.session['val2']
    guest1.no_of_children = request.session['val3']
    guest1.Identity_no = request.session['val13']
    guest1.Room_code = request.session['val700']
    guest1.No_of_nights = request.session['val6']

    guest1.save()

    ro = models.rooms.objects.all()
    for ro in ro:
        if (ro.Roomcode == request.session['val700']):
            ro.Availible = False
            ro.save()
            break
    val180 = request.session['val150']
    send_mail('Payment Received', 'Room Booked', 'raghavrudhra28@gmail.com',
              ['{}'.format(val180)], fail_silently=True)
    return render(request, "success.html")


@login_required(login_url='login')
def cancel(request):
    del request.session['val700']
    return redirect('/')
