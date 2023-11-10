from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
