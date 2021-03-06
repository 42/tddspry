from django.conf.urls.defaults import *


urlpatterns = patterns('testproject.testapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^edit_hidden_fields/$', 'edit_hidden_fields',
        name='edit_hidden_fields'),
    url(r'^login/$', 'login', name='auth_login'),
    url(r'^logout/$', 'logout', name='auth_logout'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^redirect/$', 'redirect', name='redirect'),
    url(r'^user/(?P<username>[^/]+)/$', 'user', name='user'),
    url(r'^users/$', 'users', name='users'),
)
