from django.urls import path, re_path
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views
from .views import *

app_name = "users"
urlpatterns = [
    path("login/", view=login, name="login"),
    path("create/", view=createuser, name="crear usuario"),
    path("", view=ruduser, name="obtener modificar y destruir usuario"),
    path("login-social/<str:backend>/", view=facebook, name="social-mobile-login"),
    path("user/change-password/", view=changepasswordapi),
    re_path(r'^user/recovery/(?P<id>\d+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
            {"post_reset_redirect": reverse_lazy(
                'users:password_reset_complete')},
            name='password_reset_confirm'),
    path("reset/done/", password_reset_complete, name='password_reset_complete'),
    path("user/recovery/", view=recoverypasswordapi),

]
