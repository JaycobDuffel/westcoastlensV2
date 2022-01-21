
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home.home_page, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )