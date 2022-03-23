
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import home, packages, portfolio
from portfolio.views import packages

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home.home_page, name="home"),
    path("packages/", packages.packages_page, name="packages"),
    path("portfolio/", portfolio.portfolio_page, name="portfolio"),
    path("portfolio/portraits/", portfolio.portrait_page, name="portraits"),
    path("portfolio/couplesandengagement/", portfolio.couples_page, name="couplesandengagement"),
    path("portfolio/weddingandelopement/", portfolio.wedding_page, name="weddingandelopement"),
    path("portfolio/boudoir/", portfolio.boudoir_page, name="boudoir"),

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
