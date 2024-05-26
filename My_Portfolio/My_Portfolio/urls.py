"""
URL configuration for My_Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', viewshome, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # Make sure to include this import
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from django_otp.plugins.otp_totp.models import TOTPDevice

from Portfolio.views import home_screen_view
from account.models import Account
from account.views import logout_view, login_view


class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(Account)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes the auth URLs
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login")

]

if settings.DEBUG:  # tells the application where to lok for static files when we are in debug mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Portfolio.views import home_screen_view
from account.views import logout_view, login_view, otp_verify_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('otp-verify/', otp_verify_view, name="otp_verify"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
