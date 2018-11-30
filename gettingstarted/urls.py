from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

import hello.views
from hello.views import HomeView, ChartData, handle_particle_hook, API, TempView, BatteryView, PresView, ContactView, AboutView

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view()),
    path("charts/temp/", TempView.as_view()),
    path("charts/battery/", BatteryView.as_view()),
    path("charts/pres/", PresView.as_view()),
    path("contact/", ContactView.as_view()),
    path("about/", AboutView.as_view()),
    path('api/', API.as_view()),
    path('api/chart/data/', ChartData.as_view()),
    path('api/webhook/', hello.views.handle_particle_hook, name='handle_particle_hook')

]
