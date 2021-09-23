from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from user_auth import views

router = DefaultRouter()
router.register("users", views.UserApi, basename='Users')
router.register("usersearch", views.UserInputApi, basename='UserSearch')

urlpatterns = [
    path('', views.index, name='Index'),
    path('input/', views.saveInput, name='Input'),
    path('login/', views.login_attempt, name='Login'),
    path('logout/', views.logout_attempt, name='Logout'),
    path('resister/', views.register_attempt, name='Register'),
    path('api/', include(router.urls)),
    path('token/get', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

]
