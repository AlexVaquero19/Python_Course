"""
URL configuration for my_project_activity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

#You have to take into account the order of matching 'urls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app_activity.urls')),  # Links to URLs in 'my_app'
]

"""
Wrong: the '*' match with every page we have to get into
    path('*', include('my_app_activity.urls')),  # Links to URLs in 'my_app'
    path('admin/', admin.site.urls),

Right:
    path('admin/', admin.site.urls),
    path('', include('my_app_activity.urls')),  # Links to URLs in 'my_app'
"""