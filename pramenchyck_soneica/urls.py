from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("shop.urls", namespace='shop')),
    path("about/", include("about.urls", namespace="about")),
    path("user/", include("user.urls", namespace='user')),
    path("only-staff/", include("only_staff.urls", namespace="only_staff"))
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
