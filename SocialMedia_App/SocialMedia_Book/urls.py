from django.contrib import admin
from django.urls import path
from .views import home_view, signin_view, signup_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', home_view),
    path('signup/', signup_view),
    path('signin/', signin_view)
]


urlpatterns += staticfiles_urlpatterns()