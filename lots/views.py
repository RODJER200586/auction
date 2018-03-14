from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Lot


def index(request):
    latest_lot_list = Lot.objects.order_by('-id')[:5]
    context = {'latest_lot_list': latest_lot_list}
    return render(request, 'index.html', context)


def detail(request, lot_id):
    lot = get_object_or_404(Lot, pk=lot_id)
    return render(request, 'detail.html', {'lot': lot})


def results(request, lot_id):
    response = "You're looking at the results of lot %s."
    return HttpResponse(response % lot_id)


def vote(request, lot_id):
    return HttpResponse("You're voting on lot %s." % lot_id)
