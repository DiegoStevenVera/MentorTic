from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
                  # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),
                  # User management
                  path(
                      "api/v1/users/",
                      include("apps.users.urls", namespace="users"),
                  ),
                  path(
                      "api/v1/mentors/",
                      include("apps.mentor.urls", namespace="mentors")
                  ),
                  path(
                      "api/v1/competencias/",
                      include("apps.competencia.urls", namespace="competencias")
                  ),
                  path(
                      "api/v1/entidades/",
                      include("apps.entidad.urls", namespace="entidades")
                  ),
                  path(
                      "api/v1/ubigeos/",
                      include("apps.ubigeos.urls", namespace="ubigeo")
                  ),
                  path("auth", include('rest_framework_social_oauth2.urls')),
                  re_path(r'^swagger(?P<format>\.json|\.yaml)/$', schema_view.without_ui(cache_timeout=None),
                          name='schema-json'),
                  path("swagger/", schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
                  path("redoc/", schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
                  # Your stuff: custom urls includes go here
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
