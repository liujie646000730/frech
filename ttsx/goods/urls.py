from django.conf.urls import include, url
from goods import views

urlpatterns = [

    url(r'^index$',views.index),
]