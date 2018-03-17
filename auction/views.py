from django.views import generic

from .models import Lot


class ListView(generic.ListView):
    template_name = 'lots/list.html'
    context_object_name = 'latest_lot_list'

    def get_queryset(self):
        return Lot.objects.order_by('-id')


class DetailView(generic.DetailView):
    model = Lot
    template_name = 'lots/detail.html'
