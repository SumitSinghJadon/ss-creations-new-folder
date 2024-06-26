from rest_framework import routers
from .views import *
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'ApplyLeave', LeaveViewSet)
router.register(r'ChartData', ChartDataViewSet,basename="ChartData")




urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', LoginApi.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]