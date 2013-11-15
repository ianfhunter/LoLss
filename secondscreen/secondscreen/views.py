
from django.template import RequestContext, loader
from django.http import HttpResponse
from synch.models import *

def home(request):
    template = loader.get_template('home.html')

    pad = Screen.objects.all().order_by('page_id')[0]

    context = RequestContext(request, {
    })

    return HttpResponse(template.render(context))

#For generated Unique Urls
def home2(request,unique_id):
    template = loader.get_template('index.html')

    pad = Screen.objects.all().order_by('page_id')[0]

    context = RequestContext(request, {
        "baron":pad.baron_timer,
        "dragon":pad.dragon_timer,

        "top_blue":pad.top_blue_timer,
        "top_red":pad.top_red_timer,

        "bot_blue":pad.bottom_blue_timer,
        "bot_red":pad.bottom_red_timer,

        "top_t_inhib":pad.top_inhib_tlane,
        "top_m_inhib":pad.top_inhib_mlane,
        "top_b_inhib":pad.top_inhib_blane,

        "bot_t_inhib":pad.bottom_inhib_tlane,
        "bot_m_inhib":pad.bottom_inhib_mlane,
        "bot_b_inhib":pad.bottom_inhib_blane,

        "wards": Ward.objects.filter(screen=pad)
    })

    return HttpResponse(template.render(context))


def save(request):
    return HttpResponse(template.render(context))