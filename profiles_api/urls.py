from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'profiles_api'
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UserProfileViewSet)
router.register('feed', views.UserFeedApiViewSet, basename='feed')
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view(), name='hello'),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
