from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Demo API",
        default_version="v1",
        description="",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=None,
)


urlpatterns = [
    path(
        "docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-schema-ui",
    ),
    path("admin/", admin.site.urls),
]
