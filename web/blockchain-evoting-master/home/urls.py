from django.urls import path
from home import views
app_name = 'home'
urlpatterns = [ 
    
    path('finger_login/', views.finger_login , name="finger_login"),
    path('', views.login_admin ,name="login"),
    path('logout', views.home_logout ,name="logout"),
    path('profile', views.home_profile ,name="profile"),
    path('api_login', views.api_login ,name="api_login"),

]
