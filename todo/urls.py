from django.urls import path,include
from . import views


urlpatterns=[
    path('signup/',views.signupuser , name='signupuser'),
    path('current/',views.currenttodos , name='currenttodos'),
    path('',views.homepage , name='homepage'),

    path('login/',views.loginuser , name='loginuser'),
    path('logout/',views.logoutuser , name='logoutuser'),

]