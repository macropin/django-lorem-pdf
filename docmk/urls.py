from django.conf.urls.defaults import *

urlpatterns = patterns('docmk.views',

    url(r'^html/(?P<code>[\-\d\w]+)', 'html', name='html'),
    url(r'^pdf/(?P<code>[\-\d\w]+)', 'pdf', name='pdf'),

)
