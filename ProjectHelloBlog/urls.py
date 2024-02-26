"""
URL configuration for ProjectHelloBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from HelloBlog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('cadastro/', views.cadastro),
    path('detalhes-post/<int:id>', views.detalhes_post),
    path('login-e-seguranca/', views.login_e_seguranca),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('meus-posts/', views.meus_posts),
    path('meus-comentarios/', views.meus_comentarios),
    path('minha-conta/', views.minha_conta),
    path('publicar/', views.publicar),
    path('redes-sociais/', views.redes_sociais),
    path('sobre/', views.sobre),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
