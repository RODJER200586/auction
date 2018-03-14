from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lots/', include('lots.urls')),
    path('admin/', admin.site.urls),
]
