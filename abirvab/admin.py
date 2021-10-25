from django.contrib import admin
from .models import *
# Register your models here.

modelNameList = [Content, Kobita ,  Golpo ,  Chobi ,  CinemaReview ,  BoiReview ,  RannaBanna, Probondho, BoiBahar, Other ]

for i in modelNameList:
    admin.site.register(i)