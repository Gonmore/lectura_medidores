"""
URL configuration for supernovacloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from registration import views as rviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sntmeter.urls')),
    path('registration/', include('registration.urls')),
    path('accounts/logout', rviews.logout_user , name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]

admin.site.site_header = 'SupernovaCloud'                    # default: "Django Administration"
#admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'Administracion SupernovaCloud' # default: "Django site admin"