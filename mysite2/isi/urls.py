from django.urls import path
from . import views

app_name = 'isi'

urlpatterns = [
    path('isigame',views.isi, name='isi game'),
]
