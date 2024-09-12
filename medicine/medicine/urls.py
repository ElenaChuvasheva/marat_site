from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler404 = "core.views.page_not_found"
handler403 = "core.views.csrf_failure"
handler500 = "core.views.internal_error"

urlpatterns = [
    path("", include("posts.urls", namespace="posts")),
    path("for_staff_only/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
