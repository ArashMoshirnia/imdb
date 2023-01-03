from django.urls import path
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.api.views import LoginStep1View, LoginStep2View

urlpatterns = [
    # path('login/username', views.obtain_auth_token),

    path('login/step-1/', LoginStep1View.as_view()),
    path('login/step-2/', LoginStep2View.as_view()),


    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
