from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import path

from user.views import UserCreateView, UserDetailView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserCreateView.as_view(), name='signup'),

    path('profile/<slug:pk>/', UserDetailView.as_view(), name='profile'),
]
