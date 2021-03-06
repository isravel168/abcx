"""jd_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^temp/',include('temporary.urls')),
    url(r'^api/',include('temporary.api.urls')),

    #JWT TOKEN PURPOSE

    #url(r'api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #url(r'api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')

    # AT SETTINGS
#    'DEFAULT_AUTHENTICATION_CLASSES': [
#    'rest_framework_simplejwt.authentication.JWTAuthentication',
#]
]
