
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = loader.get_template('index.html')

    context = RequestContext(request, {

    })

    return HttpResponse(template.render(context))

def save(request):
    return HttpResponse(template.render(context))