from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import companydb,curr_del,delivery_data
from django.contrib import messages
import hashlib
import smtplib
import datetime

#registeration
def register(request):
    if request.method == 'POST':
        cmpa = companydb.objects.all().last()
        if cmpa is None:
            cmp_id='C101'
        else:
            cmp_id = 'C'+str(int(cmpa.id[1:]) + 1)
        name = request.POST['name']
        email = request.POST['email']
        address = ''
        password=request.POST['password']
        cpass=request.POST['cpass']
        ema=companydb.objects.filter(email=email).exists()
        if ema is True:
            messages.error(request,'Email Already Exists')
            return render(request,"register.html")
        if len(password)<8:
            messages.error(request,'Password Must Be Minimum 8 Characters Long')
            return render(request,"register.html") 
        if cpass!=password:
            messages.error(request,'Password And Confirm Password Did Not Match')
            return render(request,"register.html") 
        password=hashlib.md5(password.encode()).hexdigest()
        companydb.objects.create(id=cmp_id, name=name,email=email,address=address,password=password)
        messages.success(request,'Account Created Successfully!! Please Login To Continue')
        return redirect('/company/')

    else:
        return render(request, 'register.html')
#login
def login(request):
    if request.session.has_key('cid'):
        id = request.session['cid']
        data=companydb.objects.get(id=id)
        return render(request, 'companyhome.html', {"data" : data})
    
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        password=hashlib.md5(password.encode()).hexdigest()
        ema=companydb.objects.filter(email=email).exists()
        if ema is False:
            messages.error(request,'Email Does Not Exist')
            return render(request,"login.html")
        ema=companydb.objects.filter(email=email,password=password).exists()
        if ema is True:
            data=companydb.objects.get(email=email,password=password)
            request.session['cid']=data.id
            return render(request,'companyhome.html',{"data":data})
        else:
            messages.error(request,'Email And Password Did Not Match')
            return render(request,"login.html")
    else:
        return render(request, 'login.html')

def logout(request):
    try:
        del request.session['cid']
    except:
        pass
    messages.error(request,'You Are Now Logged Out!! Please Login Again To Continue')
    return render(request,"login.html")

def profile(request):
    if request.session.has_key('cid'):
        id = request.session['cid']
        data=companydb.objects.get(id=id)
        add=data.address
        if add=='':
            hno,city,cntry,pin='','','',''
        else:
            add=add.split(',')
            hno,city,cntry,pin=add[0],add[1],add[2],add[3]
        return render(request,'profile.html',{"data":data,"hno":hno,"city":city,"country":cntry,"pin":pin})
    else:
        return render(request,"login.html")

def update(request):
    if request.session.has_key('cid'):
        if request.method=='POST':
            cid = request.session['cid']
            email=request.POST['email']
            name=request.POST['name']
            add=request.POST['add']+','+request.POST['city']+','+request.POST['country']+','+request.POST['pin']
            data=companydb.objects.get(id=cid)
            data.email=email
            data.name=name
            data.address=add
            data.save()
            add=add.split(',')
            hno,city,cntry,pin=add[0],add[1],add[2],add[3]
            return render(request,'profile.html',{"data":data,"hno":hno,"city":city,"country":cntry,"pin":pin})
    else:
        return render(request,'login.html')
def change(request):
    if request.session.has_key('cid'):
        id = request.session['cid']
        data=companydb.objects.get(id=id)
        return render(request,'change_pass.html',{'data':data})
    else:
        return render(request,'login.html')

def changepass(request):
    if request.session.has_key('cid'):
        if request.method=='POST':
            cid=request.session['cid']
            data=companydb.objects.get(id=cid)
            old=request.POST['opass']
            new=request.POST['npass']
            conf=request.POST['cpass']
            old=hashlib.md5(old.encode()).hexdigest()
            if data.password!=old:
                messages.error(request,'Incorrect Password')
                return render(request,'change_pass.html',{"data":data})
            if new!=conf:
                messages.error(request,'Password And Confirm Password Did Not Match')
                return render(request,'change_pass.html',{'data':data})
            if len(new)<8:
                messages.error(request,'Password Must Be At Least 8 Characters Long')
                return render(request,'change_pass.html',{'data':data})
            new=hashlib.md5(new.encode()).hexdigest()
            data.password=new
            data.save()
            messages.error(request,'Password Changed Successfully')
            return render(request,'profile.html',{'data':data})

def orders(request):
    if request.session.has_key('cid'):
        cid=request.session['cid']
        data=companydb.objects.get(id=cid)
        data1=curr_del.objects.filter(cmp_id=cid)
        return render(request,'tables.html',{'data':data,'data1':data1})

def policy(request):
    return HttpResponse("<h1>Click Nahi Karna Tha Bas Check Box Tick Krdo</hq>")

def upload(request):
    if request.session.has_key('cid'):
        cid=request.session['cid']
        data=companydb.objects.get(id=cid)
        return render(request,'del_upload.html',{'data':data})
    else:
        return render(request,'login.html')

def upload_new(request):
    if request.session.has_key('cid'):
        if request.method=='POST':
            fil_id = delivery_data.objects.all().last()
            if fil_id is None:
                fil_id='F101'
            else:
                fil_id = 'F'+str(int(fil_id.data_id[1:]) + 1)
            cid=request.session['cid']
            file=request.FILES['file']
            delivery_data.objects.create(data_id=fil_id,cmp_id=cid,new_del=file)
            messages.error(request,'File Uploaded Successfully')
            data=companydb.objects.get(id=cid)
            return render(request,'del_upload.html',{'data':data})
    else:
        return render(request,'login.html')


    
        

    
    