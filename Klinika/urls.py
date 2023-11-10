from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from register.views import *

router = DefaultRouter()
router.register('bemorlar', BemorModelViewSet)
router.register('tolovlar', TolovModelViewSet)
router.register('xulosalar', XulosaModelViewSet)
router.register('xonalar', XonaModelViewSet)
router.register('bosh_xonalar', BoshXonalarModelViewSet)
router.register('joylashtirishlar', JoylashtirishModelViewSet)
router.register('yollanmalar', YollanmaModelViewSet)
router.register('sub_yollanmalar', SubYollanmaModelViewSet)
router.register('tolov_qaytarishlar', TolovQaytarishViewSet)
router.register('cheklar', ChekModelViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Klinika API",
      default_version='v1',
      description="Odiljon Revmatolog klinikasi sotuv tizimi uchun yozilgan API",
      contact=openapi.Contact(email="1997abdulhamid@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('admin_tolovlar/', TolovlarAPIView.as_view()),
    path('sana/', HozirgiSana.as_view()),
    path('users/', UserAPIView.as_view()),
    path('hamma_xonalar/', HammaXonalarView.as_view()),
    path('user_create/', UserPostView.as_view()),
    path('user_update/<int:pk>/', UserPutAPIView.as_view()),
    path('admin_tolov/delete/<int:pk>/', TolovDeleteAPIView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
