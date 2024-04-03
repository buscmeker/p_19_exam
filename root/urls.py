
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from apps import views
from root import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_1, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)