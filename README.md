# Loremized PDF generator (Django)

If you're looking for a simple example of PDF Generation in Python / Django then you might find this interesting.

If you have to ask why, then this project is not for you :) 

## Usage

* Requests to _http://localhost:8000/pdf/<xx>.pdf_ will generate a pdf with randomised lorem content.
* Requests to _http://localhost:8000/html/<xx>.html_ will generate html with randomised lorem content.

## Installation

To make use of this awesomely random project first the setup your Django project then add the following to your Django project _urls.py_:

<pre>
    url(r'', include('docmk.urls')),
</pre>

And then add the following to your _INSTALLED_APPS_ in _settings.py_"

<pre>
    'django.contrib.webdesign',
    'docmk',
</pre>

You'll also need _adlibre-django_ for the PDF rendering code, and any other requirements:

<pre>
    pip install -e git+git://github.com/adlibre/django-adlibre.git#egg=django-adlibre
    pip install xhtml2pdf
</pre>

-- Andrew Cutler
