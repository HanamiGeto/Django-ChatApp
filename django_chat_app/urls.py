"""
URL configuration for django_chat_app project.

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
from django.urls import include, path, reverse_lazy

from chat.views import index, login_view, register_view, logout_view
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', index, name='chat'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', RedirectView.as_view(pattern_name="chat")),
    # path('', include(('django_chat_app.urls', 'chat'), namespace='chat')),
    path('logout/', logout_view, name='logout'),
    # path('^register/', CreateView.as_view(
    #     template_name='register/register.html',
    #     form_class=UserCreationForm,
    #     success_url=reverse_lazy('chat')  # note the usage of reverse_lazy here 
    # ), name='register'),
]
