from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('factory1/', include('factory1.urls', namespace='factory1')),
    path('factory2/', include('factory2.urls', namespace='factory2'))
]
