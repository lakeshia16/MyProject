from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import homepage_view, home_page


urlpatterns = [
#    path('', homepage_view, name='homepage'),
    path('', home_page),
]


# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)