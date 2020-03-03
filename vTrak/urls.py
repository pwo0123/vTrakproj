from django.urls import path

from vTrak.views import exportcsv
from . import views

urlpatterns = [
    path('', views.home, name='vTrak-home'),
    path('about', views.about, name='vTrak-about'),
    path('log', views.log, name='vTrak-log'),
    path('history', views.history, name='vTrak-history'),
    path('report', views.exportcsv, name='vTrak-exportcsv')

]
