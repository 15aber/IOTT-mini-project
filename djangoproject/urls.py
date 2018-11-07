
from django.contrib import admin
from django.urls import path, include
from mdata.views import get_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mdata/', include('mdata.urls')),
    path('api/data/', get_data, name='api-data'),

]
