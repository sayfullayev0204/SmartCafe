from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('taom/', taom, name='taom'),
    path('detail/', detail, name='detail')
]
