"""
This code should be copy and pasted into blog/urls.py
"""


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^login', 'reg.views.do_login'),
    ##url(r'^$', 'reg.views.home'),
    url(r'^logout', 'reg.views.do_logout'),
    url(r'^logout/$', 'reg.views.do_logout'),
    url(r'^error/$', 'reg.views.do_error'),
    )

    

