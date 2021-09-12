from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('store', views.store),
    path('feedback', views.feedback_base),
    path('feedback/<int:pk>/', views.feedback),
]
