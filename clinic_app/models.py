from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Speciality(models.Model):
    title = models.CharField(max_length=255)

class Doctors(models.Model):
    name = models.CharField(max_length=255)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

class Applications(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

class Services(models.Model): #написать наши услуги грязелечение физиотер и т.д.
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField()

class News(models.Model): #написать подробно про каждый вид лечения
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

class NewsImages(models.Model):
    newObject = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    

class Comments(models.Model):
    user = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    newObject = models.ForeignKey(News, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Slider(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    url = models.TextField()

class Galery(models.Model):
    image = models.ImageField()

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

class Subscriptions(models.Model):
    mail = models.TextField(max_length=250)

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=700)
    image = models.ImageField()

class MainVideo(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    video_image = models.ImageField(upload_to='videosImages/') 