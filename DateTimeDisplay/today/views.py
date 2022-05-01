from django.shortcuts import render
from datetime import date,datetime,time

# Create your views here.
def index(request):
    dt = datetime.now()   
    return render(request,'today/index.html',{'datetime':dt})