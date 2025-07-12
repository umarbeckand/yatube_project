from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SignUpView


app_name = 'users'


urlpatterns = [
 path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
]
