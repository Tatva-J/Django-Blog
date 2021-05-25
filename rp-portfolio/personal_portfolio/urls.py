from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView



urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli UR
    path("",views.Base, name="base"),
    path("admin/", admin.site.urls),
    path("projects/", include('projects.urls')),
    path("blog/", include("blog.urls")),
]