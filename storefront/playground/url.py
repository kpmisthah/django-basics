from django.urls import path
from . import views

# url conf moduled
urlPatterns = [
    path('playground/hello',views.say_Hello)
]
