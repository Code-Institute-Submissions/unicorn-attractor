"""unicorn_attractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .settings import MEDIA_ROOT
from django.views import static
from accounts import urls as urls_accounts
from home import urls as urls_home
from home.views import index
from tickets import urls as urls_tickets
from tickets.views import all_tickets
from search import urls as urls_search
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from promotions import urls as urls_promotion

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^home/', include(urls_home)),
    url(r'^tickets/', include(urls_tickets)),
    url(r'^search/', include(urls_search)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^promotion/', include(urls_promotion)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]
