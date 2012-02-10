from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

import docmk.views

urlpatterns = patterns('docmk.views',

    url(r'^html/(?P<code>[\-\d\w]+)', 'html', name='html'),
    url(r'^pdf/(?P<code>[\-\d\w]+)', 'pdf', name='pdf'),

)
