from django.shortcuts import render, HttpResponse
from django.views import generic
from .forms import searchForm
from .apiConection import *
# Create your views here.

class homePage(generic.FormView):
    def get(self, request, *args, **kwargs):

        context = {"locations": getLocation()}
        template_name = "home.html"
        return render(request, template_name,context)
    def post(self, request, *args, **kwargs):
        form = request.POST
        return HttpResponse("{0}".format(form))
# def index(request):
#     return render(request, "home.html")