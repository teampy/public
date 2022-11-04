
from django.contrib import admin
from django.urls import path
from took.views import home,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contact',contact,name='contact'),
]
