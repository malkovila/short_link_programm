from django.urls import path, include
from. import views


urlpatterns = [
    path("reg/", views.registry, name="registry"),
    path('check_info/', views.check_info, name="ch_info"),
    path('make_reg/', views.make_register, name='mr'),
    path('', views.login, name='login'),

]