"""django_lesson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('main', views.main),
    path('interier_dolls', views.interier_dolls),
    path('for_game', views.for_game),
    path('dress', views.dress),
    path('contacts', views.contacts),
    path('longleg', views.longleg),
    path('angel', views.angel),
    path('cool_girl', views.cool_girl),
    path('butterfly', views.butterfly),
    path('school', views.school)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
