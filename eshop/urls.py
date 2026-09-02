from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls'))
] 


# Serve media files only during local development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)