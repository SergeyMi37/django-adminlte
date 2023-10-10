from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path(r'set-language/', views.set_language, name='set_language'),
]
