from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LogoutView

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # login
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # obtain a new Access Token from Refresh Token
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
