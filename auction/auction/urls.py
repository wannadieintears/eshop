from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('bboard.urls')),
    path('advertisement/', include('advertisement.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
]
