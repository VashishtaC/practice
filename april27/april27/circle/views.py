from django.shortcuts import render
from .forms import circle_detail
def circle(request):
    c1=circle_detail()
    return render(request,'index.html',{'circle':c1})

# Create your views here.
