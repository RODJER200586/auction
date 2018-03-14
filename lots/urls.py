from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:lot_id>/', views.detail, name='detail'),
    path('<int:lot_id>/results/', views.results, name='results'),
    path('<int:lot_id>/vote/', views.vote, name='vote'),
]
