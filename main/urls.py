from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('contacts/', views.ContactsView.as_view()),
    path('accounts/profile/', views.ProfileView.as_view()),
]
