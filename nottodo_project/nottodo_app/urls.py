from django.urls import path,include
from .views import UserCreate
from rest_framework.routers import DefaultRouter
from .views import NotTODOViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'nottodos', NotTODOViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-create'),
    path('', include(router.urls)),
]
