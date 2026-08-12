from django.urls import path
from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.order, name='order'),
    path("feedback/", views.feedback, name="feedback"),
]