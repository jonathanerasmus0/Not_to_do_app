from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nottodo_app.views import NotTODOViewSet, CommentViewSet, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'nottodos', NotTODOViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserCreate.as_view(), name='user-create'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),
]
