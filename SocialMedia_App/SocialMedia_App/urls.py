from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SocialMedia_Book.urls'))
]

urlpatterns += staticfiles_urlpatterns()