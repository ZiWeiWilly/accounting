from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:credit_id>/', views.credit_no, name='credit_no'),
]
