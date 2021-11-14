from django.shortcuts import render
from .forms import Details
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from django.views.generic import View
from xhtml2pdf import pisa
 

def result(request):
    if request.method=="POST":
        SName=request.POST['sname']
        SPhone=request.POST['sphone']
        SAddress=request.POST['saddress']
        CName=request.POST['cname']
        CPhone=request.POST['cphone']
        CAddress=request.POST['caddress']
        I1=request.POST['item1']
        Q1=request.POST['quantity1']
        A1=request.POST['price1']
        I2=request.POST['item2']
        Q2=request.POST['quantity2']
        A2=request.POST['price2']    
    
    return render(request,"result.html",{'sn':SName,'sp':SPhone,'sa':SAddress,'cn':CName,'cp':CPhone,'ca':CAddress,'i1':I1,'q1':Q1,'a1':A1,'i2':I2,'q2':Q2,'a2':A2})


def index(request):
    d=Details()
    return render(request,'index.html',{'form':d})


                
        

