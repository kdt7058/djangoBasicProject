from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index1"),
    path('about', views.about, name="about1"),
    path('home', views.home, name="home1"),
    path('punc', views.punc, name="punc1"),

]
