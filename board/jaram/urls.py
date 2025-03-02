from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jaram'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', views.post_create, name='post-create'),
    path('posts/<int:pk>/edit/', views.post_update, name='post-update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)