from django.shortcuts import render
from .forms import Details
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from django.views.generic import View

#imports to generate pdf
from xhtml2pdf import pisa
from django.template.loader import get_template


# To render data into a pdf and dynamically download the pdf
def render_pdf_view(request,data):
    
    template_path='result.html' #html file to be used for printing 
    context=data
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename="invoice.pdf"'    #you can change file name here

    template=get_template(template_path)
    #print(context)
    html=template.render(context)
    #print(html)
    pisa_status=pisa.CreatePDF(html,dest=response)

    if pisa_status.err:
        return HttpResponse('We had some error ')
    print(response)
    return response


def result(request):
    if request.method=="POST":
        sno=request.POST['id']
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
        d=request.POST['date']  
    
        data={'i':sno,'sn':SName,'sp':SPhone,'sa':SAddress,'cn':CName,'cp':CPhone,'ca':CAddress,'i1':I1,'q1':Q1,'a1':A1,'i2':I2,'q2':Q2,'a2':A2,'da':d} 

        return render_pdf_view(request,data)
    
    return render(request,"result.html")
  

def index(request):
    d=Details()
    return render(request,'index.html',{'form':d})

  



                
        

              
        

