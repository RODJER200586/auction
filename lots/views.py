from django.http import HttpResponse


def index(request):
    return HttpResponse("Lots list")


def detail(request, lot_id):
    return HttpResponse("You're looking at lot %s." % lot_id)


def results(request, lot_id):
    response = "You're looking at the results of lot %s."
    return HttpResponse(response % lot_id)


def vote(request, lot_id):
    return HttpResponse("You're voting on lot %s." % lot_id)
