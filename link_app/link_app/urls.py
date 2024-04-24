
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from links.views import ApiLinks
from users import views as v
from links import views

router = routers.DefaultRouter()
router.register(r'api/Link', ApiLinks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include(router.urls)),
    path('cabinet/', include('links.urls')),
    path('<str:link>/', views.zapros),


]
