from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pic/', include('pic.urls')),
    path('admin/', admin.site.urls),
]