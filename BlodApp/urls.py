from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('requests/', include("requests.urls")),
    path('screening/', include("screening.urls")),
    path('donor/', include("Donor.urls")),
    url("", include("allauth.urls")), 
]
