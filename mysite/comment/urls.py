from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.form),
    path('about/',views.about),
    path('comments/',views.comment)

]
