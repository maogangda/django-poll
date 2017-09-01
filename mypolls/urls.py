from django.conf.urls import include, url
from django.contrib import admin
from views import index,show,showAction

urlpatterns = [
    # Examples:
    # url(r'^$', 'xtoupiao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', index,name='index'),
    url(r'^show/(?P<id>[0-9]+)',show,name='show'),
    url(r'^showAction(?P<id>[0-9]+)',showAction,name='showAction')


]
