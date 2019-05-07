from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mysocial import views as user_views
from rest_framework.urlpatterns import format_suffix_patterns
from mysocial import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysocial.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='mysocial/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mysocial/logout.html'), name='logout'),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/apilogin/', views.apilogin),
]
urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)