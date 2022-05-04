from django.urls import path
from mainmenu import views
app_name = 'mainmenu'
urlpatterns = [ 
    path('menu_list', views.menu_list , name="menu_list"),
    path('menu_create', views.menu_create , name="menu_create"),
    path('link_list', views.link_list , name="link_list"),
    path('link_create', views.link_create , name="link_create"),
]
