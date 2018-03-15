from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lots/', include('auction.urls')),
    path('admin/', admin.site.urls),
]
