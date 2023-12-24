from django.shortcuts import render
from .models import *
from django.shortcuts import HttpResponse
import os
# import requests
from django.views.generic.edit import CreateView 
from django.core.paginator import Paginator 
from django.http import JsonResponse
from datetime import datetime
# Create your views here.

def index(request):
    application = Speciality.objects.all()
    galery = Galery.objects.all()

    context = {
        'application':application,
        'galery': galery
    }
    
    context['slider'] = Slider.objects.all()
    context['services'] = Services.objects.all()[:4]
    context['news'] = News.objects.all()[:3]

    return render(request, 'index.html', context)
    
    
def saveApplicat(request):

    if request.method == 'POST':
        speciality_id = int(request.POST.get('speciality'))

        speciality = Speciality.objects.get(id = speciality_id)
        
        doctor_id = request.POST.get('doctor')
        doctor = Doctors.objects.get(id = doctor_id)
        
        date = datetime.strptime(request.POST.get('date'), '%d/%m/%Y')
        date =date.strftime('%Y-%m-%d')
        time = request.POST.get('time')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        row = Applications.objects.create(speciality = speciality, doctor = doctor, date = date, time= time, name = name, phone = phone, email = email, message = message)
        row.save()
    return index(request)


def services(request):
    service = Services.objects.all()
    context = {
        'service':service
    }
    return render(request, 'services.html', context)

def news(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')

    page = 1
    if request.GET.get('page'):
        page = int(request.GET.get('page'))

    rows = News.objects.all()
    paginator = Paginator(rows, 6)

    next_page = page + 1 if (page + 1) <= len(paginator.page_range) else page
    previous_page = page - 1 if (page - 1) != 0 else page

    
    # news = News.objects.all()
    
    context = {
        'rows': rows,
        'result_count': f"Показано {6} из {len(rows)}",
        'news': paginator.page(page),
        'pages': paginator.page_range, 
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
    }

    context['latestNews'] = News.objects.order_by('-created_at')[:3]

    return render(request, 'blog.html', context)

def newsDetails(request, id):
    row = News.objects.get(id=id)
    images = NewsImages.objects.filter(newObject=row)
    comments = Comments.objects.filter(newObject=row)
    context = {
        'row': row,
        'images':images,
        'comments':comments
    }
    return render (request, 'single-blog.html', context)

def comments(request, id):

    if request.method == 'POST':
        user = request.POST.get('user')
        email = request.POST.get('email')
        message = request.POST.get('message')
        new = News.objects.get(id=id)
        row = Comments.objects.create(user = user, email=email, message = message, newObject = new)
        row.save()
    return newsDetails(request, id)

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        row = Applications.objects.create(name = name, email = email, message = message)
        row.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about-us.html')




def get_doctors(request, speciality_id):
    doctors = Doctors.objects.filter(speciality_id=speciality_id).values('id', 'name')
    return JsonResponse(list(doctors), safe=False)