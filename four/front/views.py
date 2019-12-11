from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.
def index(request):
    # html=render_to_string("index.html")
    # return HttpResponse(html)
    return render(request,'index.html')