from django.urls import path,include
from rest_framework import routers
from testapp.API.views import RegistrationCRUDCBV
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('registerationinfo', RegistrationCRUDCBV)   #Define defualt routers

urlpatterns = [
    path('', include(router.urls)),     #Define defualt urls
    path('get-api-token', views.obtain_auth_token, name='get-api-token'),
]