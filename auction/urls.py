from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='lots'),
    path('<int:pk>/', views.DetailView.as_view(), name='lot_detail'),
]
