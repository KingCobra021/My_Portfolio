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
from django.urls import path, include
from Portfolio.views import home_screen_view
from account.views import logout_view, login_view, otp_verify_view
from django.shortcuts import redirect

def admin_redirect_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('/admin/')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect-admin/', admin_redirect_view, name='redirect_admin'),
    path('', home_screen_view, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('otp-verify/', otp_verify_view, name="otp_verify"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Portfolio.views import home_screen_view
from account.views import logout_view, login_view, otp_verify_view
from django.shortcuts import redirect

# Redirect to /admin for authenticated users
def admin_redirect_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page
    return redirect('/admin/')  # Allow access to admin panel if authenticated

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('redirect-admin/', admin_redirect_view, name='redirect_admin'),  # Custom redirect for admin access
    path('', home_screen_view, name="home"),  # Homepage
    path('accounts/', include('django.contrib.auth.urls')),  # Auth-related URLs
    path('logout/', logout_view, name="logout"),  # Logout view
    path('login/', login_view, name="login"),  # Login view
    path('otp-verify/', otp_verify_view, name="otp_verify"),  # OTP verification view
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
