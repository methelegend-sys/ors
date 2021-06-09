from django.shortcuts import render
from django.http import HttpResponse
from .models import admindb,deliveryexec
from company.models import companydb
import hashlib
from django.contrib import messages

def login(request):
    if request.session.has_key('id'):
        id = request.session['id']
        admin=admindb.objects.get(id=id)
        adminall=admindb.objects.all()
        company=companydb.objects.all().order_by('id')
        de=deliveryexec.objects.all().order_by('id')
        return render(request,'admin1/index.html',{'admin':admin,'company':company,'adminall':adminall,'de':de})
    
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        password=hashlib.md5(password.encode()).hexdigest()
        ema=admindb.objects.filter(email=email).exists()
        if ema is False:
            messages.error(request,'Email Does Not Exist')
            return render(request, 'login.html',{'title':'Admin'})
        ema=admindb.objects.filter(email=email,password=password).exists()
        if ema is True:
            admin=admindb.objects.get(email=email,password=password)
            request.session['id']=admin.id
            adminall=admindb.objects.all()
            company=companydb.objects.all().order_by('id')
            return render(request,'admin1/index.html',{'admin':admin,'company':company,'adminall':adminall})
        else:
            messages.error(request,'Email And Password Did Not Match')
            return render(request, 'login.html',{'title':'Admin'})
    else:
        return render(request, 'login.html',{'title':'Admin'})

# Create your views here.
def addde(request):
    if request.session.has_key('id'):
        id = request.session['id']
        admin=admindb.objects.get(id=id)
        return render(request,'admin1/addde.html',{'admin':admin,'title':'Admin'})
    else:
        return render(request, 'login.html',{'title':'Admin'})

def demo(request):
    if request.session.has_key('id'):
        id = request.session['id']
        admin=admindb.objects.get(id=id)
        return render(request,'admin1/addcmp.html',{'admin':admin,'title':'Admin'})
    else:
        return render(request, 'login.html',{'title':'Admin'})


