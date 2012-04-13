from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from adlibre.pdf.generate_pdf import generate_pdf

def html(request, code, template='lorem_pdf.html'):
    context = { 'code': code, }
    return render_to_response(template, context, context_instance=RequestContext(request))


def pdf(request, code, template='docmk.html'):

    context = { 'code': code, }

    try:
        pdf_result = generate_pdf(template, context)
        response = HttpResponse(pdf_result, mimetype='application/pdf')
        response['Content-Disposition'] = 'filename=%s.pdf' % (code,)
        return response
    except Exception, e:
        #raise Exception(e)
        return HttpResponse('PDF Generation Failed!')
