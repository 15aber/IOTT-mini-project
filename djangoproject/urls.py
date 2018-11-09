
from django.contrib import admin
from django.urls import path, include
from mdata.views import get_data
from mdata.views import webhook_receiver


urlpatterns = [
    path('', include('mdata.urls')),
    path('admin/', admin.site.urls),
    path('mdata/', include('mdata.urls')),
    path('api/data/', get_data, name='api-data'),
    path('webhook/', webhook_receiver, name='webhook_receiver'),

]
