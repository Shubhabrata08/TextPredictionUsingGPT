from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'home.html')

def gpt1(request):
    return render(request,'gpt1.html')

def gpt2(request):
    return render(request,'gpt2.html')
