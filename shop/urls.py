from django.contrib import admin
from django.urls import path, include
from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('core.urls')),
    path('item/', include('item.urls')),
    path('dashboard', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('inbox/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
