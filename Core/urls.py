from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_menu.urls')),
    path('users/', include('app_users.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
