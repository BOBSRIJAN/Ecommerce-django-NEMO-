
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('LA1.urls'), name="home"),
    path('accounts/', include('allauth.urls')),
]
 