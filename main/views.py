from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import *

# def index(request):
#     posts = Boat.objects.all()
#     return render(request, 'main/index.html', {'posts': posts, 'title': 'laksdjfhlskjdg',})
#
# def about(request):
#     return render(request, 'main/about.html', {"mainmenu": [1, 2, 3, 4], 'title': 'laksdjfhlskjdg',})

def home(request):
    page = Page.objects.get(title='Home')
    return render(request, 'home.html', {'content': page.content})

def boats(request):
    page = Page.objects.get(title='Boats')
    return render(request, 'boats.html', {'content': page.content})

def cruises(request):
    page = Page.objects.get(title='Cruises')
    return render(request, 'cruises.html', {'content': page.content})

def profile(request):
    page = Page.objects.get(title='Profile')
    return render(request, 'profile.html', {'content': page.content})


def boat_list_view(request):
    boats = Boat.objects.all()
    paginator = Paginator(boats, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookings/boat_list.html', {'page_obj': page_obj})

def tours_list_view(request):
    tours = Booking.objects.all()
    paginator = Paginator(tours, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookings/index.html', {'page_obj': page_obj})


def boat_detail(request, id):
    boat = get_object_or_404(Boat, id=id)
    return render(request, 'bookings/tour_detail.html', {'boat': boat})


def tour_detail(request, id):
    tour = get_object_or_404(Booking, id=id)
    return render(request, 'bookings/tour_detail.html', {'tour': tour})
