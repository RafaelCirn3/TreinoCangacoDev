from django.http import HttpResponse
from django.template import loader
from app.models import Curiosidade

def index(request):
    curiosidades = Curiosidade.objects.all()[:4]
    template = loader.get_template("index.html")
    context = {
        "curiosidades": curiosidades,
    }
    return HttpResponse(template.render(context, request))