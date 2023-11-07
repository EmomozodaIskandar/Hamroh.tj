from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Locations
from .forms import searchForm
# Create your views here.

class homePage(generic.FormView):
    def get(self, request, *args, **kwargs):
        locations = Locations.objects.all()
        context = {"locations": locations}
        template_name = "home.html"
        return render(request, template_name,context)
    def post(self, request, *args, **kwargs):
        form = request.POST
        return HttpResponse("{0}".format(form))
# def index(request):
#     return render(request, "home.html")