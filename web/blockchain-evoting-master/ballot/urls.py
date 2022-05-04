from django.urls import path
from . import views

app_name = 'ballot'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('seal/', views.seal, name='seal'),
    path('create_candidate/', views.CreateCandidate.as_view(), name='create_candidate'),
    path('delete_candidate/', views.delete_candidate, name='delete_candidate'),


]   
