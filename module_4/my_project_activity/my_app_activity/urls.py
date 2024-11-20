from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('others/', views.others, name='others'),
    path('authors/', views.author_view, name='author_view'),
    path('users/', views.users_view, name='users_view'),
    path('profile/', views.profile, name='profile'),
    path('about_2/', views.about_2, name='about_2'),
    path('base_with_logo/', views.base_with_logo, name='base_with_logo'),
    path('base_with_js/', views.base_with_js, name='base_with_js'),
    path('api_data/', views.api_data, name='api_data'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('protected_profile/', views.protected_profile, name='protected_profile'),
    path('modify_user/', views.modify_user, name='modify_user'),
    path('api_authors/', views.AuthorListCreateView.as_view(), name='author-list-create'),
    path('api_authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
