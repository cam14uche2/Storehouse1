from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Storehouse.urls')),
    path('USER_AUTH/', include('django.contrib.auth.urls')),
    path('USER_AUTH/', include('USER_AUTH.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
