from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:id>', views.cabinet, name='cabinet'),
    path('make_link/', views.make_link),
    path('show_links/<int:id>', views.show_links),
    path('links/', views.user_links, name='links'),

]