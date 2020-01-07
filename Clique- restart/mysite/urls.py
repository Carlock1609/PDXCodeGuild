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


# static media photos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('inbox/', include('messenger.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('admin/', admin.site.urls),
]

# easier to understand instead of directly adding to ulrpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# from django.conf.urls import url, include
# from django.contrib import admin
# from django.contrib.auth import views as auth_views

# from mysite.core import views as core_views

# urlpatterns = [
#     url(r'^$', core_views.home, name='home'),
#     url(r'^login/$', auth_views.login, name='login'),
#     url(r'^logout/$', auth_views.logout, name='logout'),
#     url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
#     url(r'^admin/', admin.site.urls),
# ]