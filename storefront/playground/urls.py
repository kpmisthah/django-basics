from django.urls import path
from . import views

# url conf moduled
urlpatterns = [
    path('hello/',views.say_Hello)
]
