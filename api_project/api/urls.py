from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
# Note: Ensure you import other views (BookListCreateAPIView, etc.) if you still intend to use them.

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    
    path('', include(router.urls)),
]