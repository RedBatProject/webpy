from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
  date = datetime.datetime.now()
  hh = [1,1,1,2,2,2]
  # r = {'r': hh}
  return render(request,'index.html',{'hh':date})

def main2(request):
  return  render(request,'main2.html')