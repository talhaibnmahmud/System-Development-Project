"""rentalbd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar

from django.conf.urls.static import settings, static
from django.contrib import admin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls.conf import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', include('house.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('messages/', include('chat.urls')),
    path('user/', include('user.urls')),

    path('accounts/reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('accounts/reset-password-sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset-password-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('__debug__/', include(debug_toolbar.urls)),

    # path('sw.js', (TemplateView.as_view(template_name='sw.js', content_type='application/javascript')), name='sw'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
