"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
# THIS IS USED FOR WHEN UNAUTH USERS VISIT PROFILE?
from users import views as user_views

# static media photos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.html'), name='home'),
    path('register/', user_views.register, name="register"),
    path('admin/', admin.site.urls),
]

# easier to understand instead of directly adding to ulrpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)