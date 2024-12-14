from django.urls import path
from .views import home,service_detail,protfolio_detail
app_name = 'home'
urlpatterns = [
    path('',home,name='home'),
    path('/service_detail/',service_detail,name='service_detail'),
    path('/protfolio_detail/',protfolio_detail,name='protfolio_detail')
]