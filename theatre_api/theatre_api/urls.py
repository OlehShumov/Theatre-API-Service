from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/theatre/", include("theatre.urls"), name="theatre"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/dic/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

