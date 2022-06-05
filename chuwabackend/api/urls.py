from django.urls import path, include
from .views import FileViewSet, TestAPIViewSet, TimeEventView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'test-files', FileViewSet, basename='upload')
router.register(r'api/test', TestAPIViewSet, basename='testapi')

urlpatterns = [
    path('app/', include(router.urls)),
    path('', TimeEventView.as_view(), name='app'),
]
