from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home),
    path('slot-details/<str:pk>/<str:qk>/<str:rk>', views.slotDetails,name='slot_details'),
    path('upload/',views.upload,name="upload")
    # path()

   
]