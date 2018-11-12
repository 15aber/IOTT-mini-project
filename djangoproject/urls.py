from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import mdata.views
from mdata.views import HomeView, ChartData, handle_particle_hook, API

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    #path("", hello.views.handle_particle_hook, name="index"),
    #path("db/", mdata.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name = "home"),
    path('api/', API.as_view()),
    path('api/chart/data/', ChartData.as_view()),
    path('api/webhook/', mdata.views.handle_particle_hook, name='handle_particle_hook')

]
