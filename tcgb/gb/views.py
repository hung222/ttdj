from django.http import HttpResponse
from django.template import loader
 
from .models import gb 
 
def index(request):
    gb = gb
    template = loader.get_template('index.html')
    context = {
        'gb': gb,
    }
    return HttpResponse(template.render(context, request))