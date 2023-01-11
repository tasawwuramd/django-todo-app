from django.urls import path,include
from . import views


urlpatterns=[
    path('signup/',views.signupuser),
    path('current/',views.currenttodos , name='currenttodos'),
]