from django.conf.urls.defaults import *

urlpatterns = patterns('lorem_pdf.views',

    url(r'^html/(?P<code>[\-\d\w]+)', 'html', name='html'),
    url(r'^pdf/(?P<code>[\-\d\w]+)', 'pdf', name='pdf'),

)
