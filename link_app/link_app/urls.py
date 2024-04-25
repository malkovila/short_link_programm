
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from links.views import ApiLinks
from users import views as v
from links import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/Link/<int:owner_id>/', views.ApiLinks.as_view()),
    path('cabinet/', include('links.urls')),
    path('<str:link>/', views.zapros),


]
