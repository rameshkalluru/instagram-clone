from django.contrib import admin
from django.urls import path



from core.views import login_view, register_view, logout_view

urlpatterns = [
   
    path('login/', login_view,name='login'),
    path('register/', register_view,name='signup'),
    path('logout/', logout_view,name='logout')
]