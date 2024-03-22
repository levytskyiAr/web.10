from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('author/Jane-Austen/', views.Jane_Austen, name='Jane_Austen'),
    path('author/Albert-Einstein/', views.Albert_einstein, name='Albert_einstein'),
    path('author/J-K-Rowling/', views.Rowling, name='Rowling'),
    path('author/Andre-Gide/', views.Andre_Gide, name='Andre_Gide'),
    path('author/Marilyn-Monroe/', views.Marilyn_Monroe, name='Marilyn_Monroe'),
]
