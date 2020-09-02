from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def credit_no(request, credit_id):
    return HttpResponse("You're looking at credit %s." % credit_id)
