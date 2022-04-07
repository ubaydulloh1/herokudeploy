
from django.http import HttpResponse


def homePage(request):
  return HttpResponse(request, "This is working!")