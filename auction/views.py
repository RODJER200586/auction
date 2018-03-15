from django.http import HttpResponse
from django.views import generic

from .models import Lot


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_lot_list'

    def get_queryset(self):
        return Lot.objects.order_by('-id')[:5]


class DetailView(generic.DetailView):
    model = Lot
    template_name = 'detail.html'


def results(request, lot_id):
    response = "You're looking at the results of lot %s."
    return HttpResponse(response % lot_id)


def vote(request, lot_id):
    return HttpResponse("You're voting on lot %s." % lot_id)
