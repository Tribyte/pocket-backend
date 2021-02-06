from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_views
from django.urls import path, include
from api.router import router
from api.viewsets import UserAPIView, RegisterAPIView, LoginAPIView 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('oauth/finish/', views.oauth, name='home'),
    path('api/logout', views.logout, name="logout"),
    path('api/auth/user', UserAPIView.as_view()),
    path('api/auth/register', RegisterAPIView.as_view()),
    path('api/auth/login', LoginAPIView.as_view()),
    url(r'^api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)