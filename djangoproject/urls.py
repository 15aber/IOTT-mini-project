
from django.contrib import admin
from django.urls import path, include
from mdata.views import get_data
from mdata.views import webhook_receiver, ChartData, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('mdata/', include('mdata.urls')),
    path('api/data/', get_data, name='api-data'),
    path('webhook/', webhook_receiver, name='webhook_receiver'),
    path('api/chart/data/', ChartData.as_view())

]
