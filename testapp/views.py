from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def index(request):
    name = "Rajma"
    return render(request,'ot/templates/index.html',{'name':name})


def counter(request):
    text1 = request.POST['text']
    # text1 = request.GET['text']
    print(text1)
    count_words = len(text1.split())
    return render(request,'ot/templates/counter.html',{'count':count_words})