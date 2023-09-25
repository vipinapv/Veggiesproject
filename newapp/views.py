from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
import os
import os

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout

def registration(request):
    if request.method == 'POST':
        a=regform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            un=a.cleaned_data['uname']
            em=a.cleaned_data['email']
            adr=a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            ps=a.cleaned_data['password']
            cps=a.cleaned_data['cpassword']

            b = regmodel.objects.all()
            for i in b:
                if em == i.email or un == i.uname:
                    return redirect(alreadyuser)

            if ps==cps:

                c=regmodel(fname=fn,lname=ln,uname=un,email=em,address=adr,phone=ph,password=ps,cpassword=cps)
                c.save()
                subject = "your VeGGieS account has been created"
                message = f"your VeGGieS account has been created successfully"  # f formatter to denote ac is a variable
                email_from = 'vipiluminarbank@gmail.com'
                email_to = em
                send_mail(subject, message, email_from, [email_to])
                return redirect(login)

            else:
                return HttpResponse("password and confirm password does not match")

    return render(request,'regisration.html')

# Create your views here.



def login(request):
    if request.method == "POST":
        a = logform(request.POST)
        if a.is_valid():
            un = a.cleaned_data['uname']
            ps = a.cleaned_data['password']

            b = regmodel.objects.all()
            for i in b:
                if i.uname == un and i.password == ps:
                    request.session['id']=i.id

                    return redirect(userdisplay)
            else:
                return redirect(loginfailed)

    return render(request,'userlogin.html')


def profile(request):
    try:
        id1=request.session['id']
        a=regmodel.objects.get(id=id1)
        # img=str(a.image1).split('/')[-1]
        return render(request,'profile.html',{'a':a})
    except:
        return redirect(login)
def users(request):
    try:
        id1=request.session['id']
        a=regmodel.objects.get(id=id1)
        # img=str(a.image1).split('/')[-1]
        return render(request,'user.html',{'a':a})
    except:
        return redirect(login)
def adminlogin(request):
    if request.method=="POST":
        a=adminform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            b=User.objects.all()
            user=authenticate(request,username=us,password=ps)
            if user is not None:
                return redirect(productdisplay)
            else:
                return HttpResponse("login failed....")


    return render(request,'adminlogin.html')



def productupload(request):
    if request.method=='POST':
        a=productform(request.POST,request.FILES)
        if a.is_valid():
            pn=a.cleaned_data['productname']
            pp=a.cleaned_data['price']
            pid=a.cleaned_data['productid']
            des=a.cleaned_data['description']
            fl=a.cleaned_data['file']
            p = productmodel.objects.all()
            for i in p:
                if pid == i.productid:
                    return redirect(alreadyproduct)

            b=productmodel(productname=pn,price=pp,productid=pid,description=des,file=fl)
            b.save()
            return redirect(productdisplay)
        else:
            return HttpResponse("File upload Failed...")
    return render(request,'productupload.html')



def productdisplay(request):

    a=productmodel.objects.all()
    pname=[]
    # pid=[]
    price=[]
    dis=[]
    img=[]
    id1=[]
    for i in a:
        id=i.id
        id1.append(id)
        pm=i.productname
        pname.append(pm)
        # pd=i.productid
        # pid.append(pd)
        p=i.price
        price.append(p)
        d=i.description
        dis.append(d)
        im=str(i.file).split('/')[-1]
        img.append(im)
    pair=zip(pname,price,dis,img,id1)
    return render(request,'productdisplay.html',{'list':pair})


def carddelete(request,id):
    a=productmodel.objects.get(id=id)
    os.remove(str(a.file))#used to remove the path from static
    a.delete()
    return redirect(productdisplay)

def productdelete(request,id):
    a=productmodel.objects.get(id=id)
    os.remove(str(a.file))#used to remove the path from static
    a.delete()
    return redirect(productdisplay)


def productedit(request,id):
    a=productmodel.objects.get(id=id)
    img=str(a.file).split('/')[-1]
    if request.method=='POST':
        a.productname=request.POST.get('productname')
        a.price = request.POST.get('price')
        a.productid=request.POST.get('productid')
        a.description = request.POST.get('description')
        # image
        if len(request.FILES)!=0:#new file checking
            if len(a.file)!=0:#old file checking
                os.remove(a.file.path)#remove old file using os
            a.file=request.FILES['file']
        a.save()
        return redirect(productdisplay)

    return render(request,'productedit.html',{'a':a,'img':img})

def logoutmain(request):
    logout(request)
    return redirect(login)

def logoutadmin(request):
    logout(request)
    return redirect(index)

def index(request):
    return render(request,'index.html')

def adminpage(request):
    try:
        return render(request,'adminpage.html')
    except:
        return redirect(adminlogin)
def indexnew(request):
    # try:
        id1 = request.session['id']
        a = productmodel.objects.get(id=id1)
        img=str(a.file).split('/')[-1]
        return render(request, 'indexnew.html', {'a': a,'img':img})
    # except:
        # return redirect(login)

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def onion(request):
    return render(request,'onion.html')
def chilly(request):
    return render(request,'chilly.html')
def potato(request):
    return render(request,'potato.html')
def cabbage(request):
    return render(request,'cabbage.html')

def leaves(request):
    return render(request,'leaves.html')
def brinjal(request):
    return render(request,'brinjal.html')
def payar(request):
    return render(request,'payar.html')

def others(request):
    return render(request,'others.html')



def cart1(request,id):
    a=productmodel.objects.get(id=id)
    wish=cart.objects.all()
    for i in wish:
        if i.productid==a.productid and i.uid==request.session['id']:
            return redirect(alreadycart)

    b=cart(productname=a.productname,productid=a.productid,price=a.price,productdescription=a.description,file=a.file,uid=request.session['id'])
    b.save()
    # return HttpResponse("added to cart")
    return redirect(cartdisplay)



def cartdisplay(request):


    b = cart.objects.all()
    id=request.session['id']
    # img = str(b.file).split('/')[-1]
    return render(request,'cartdisplay.html',{'b':b,'id':id})


def cartdelete(request,id):
    a = cart.objects.get(id=id)
    wish=cart.objects.all()
    # for i in wish:
    #     if i.productid == a.id and i.uid == request.session['id']:
    a.delete()
            # os.remove()
    return redirect(cartdisplay)



def forgotpassword(request):
    a=regmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        un=request.POST.get('uname')
        for i in a:
            if(i.email==em and i.uname==un):
                id=i.id
                subject="password change"
                message=f"http://127.0.0.1:8000/newapp/change/{id}"
                frm='vipiluminarbank@gmail.com'
                to=em
                send_mail(subject,message,frm,[to])
                return redirect(checkemail)
        else:
            return redirect(checkerror)
    return render(request,'forgot.html')

def change(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('password')
        p2=request.POST.get('cpassword')
        if p1==p2:
            a.password=p1
            a.save()
            return redirect(changed)
        else:
            return HttpResponse("sorry...")
    return render(request,'change.html')


def userdisplay(request):
    try:
        id1=request.session['id']
        a=productmodel.objects.all()
        pname=[]
    # pid=[]
        price=[]
        dis=[]
        img=[]
        id1=[]
        for i in a:
            id=i.id
            id1.append(id)
            pm=i.productname
            pname.append(pm)
     # pd=i.productid
        # pid.append(pd)
            p=i.price
            price.append(p)
            d=i.description
            dis.append(d)
            im=str(i.file).split('/')[-1]
            img.append(im)
        pair=zip(pname,price,dis,img,id1)
        return render(request,'userdisplay.html',{'list':pair})
    except:
        return redirect(login)

# classbased programs




class filedisplay(generic.ListView):
    model = productmodel
    template_name = 'filedisplay.html'
    def get(self,request):
        a=self.model.objects.all()
        pname=[]
        pid=[]
        des=[]
        pric=[]
        image=[]
        id1=[]
        for i in a:
            id=i.id
            id1.append(id)
            im=str(i.file).split('/')[-1]
            image.append(im)
            nm=i.productname
            pname.append(nm)
            pd=i.productid
            pid.append(pd)
            pz=i.price
            pric.append(pz)
            ds=i.description
            des.append(ds)

        mylist=zip(image,id1,pname,pid,des,pric)
        return render(request,self.template_name,{'a':mylist})



class fileview(generic.DetailView):
    model = productmodel
    template_name = 'fileview.html'
    def get(self,request,**kwargs):
        val=kwargs.get('pk')#get fn used to get value in a key value pair
        a=self.model.objects.get(id=val)
        nm=a.productname
        pid=a.productid
        des=a.description
        pr=a.price
        img=str(a.file).split('/')[-1]
        return render(request,'fileview.html',{'img':img,'nm':nm,'pid':pid,'des':des,'pr':pr})


def buyfunction1(request,id):
    x=productmodel.objects.get(id=id)
    # y=regmodel.objects.get(id=id)


    if request.method == 'POST':
        # y.uname=request.POST.get('uname')
        # y.address=request.POST.get('address')
        # y.phone=request.POST.get('phone')
        x.price = request.POST.get('price')


        # x.save()

        a=buyform(request.POST,request.FILES)
        if a.is_valid():

            un=a.cleaned_data['uname']
            adr=a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            pr=a.cleaned_data['price']
            # pm=a.cleaned_data['modep']
            b = buy(uname=un,address=adr,phone=ph,price=pr)
            b.save()
            return redirect(confirm)
        return HttpResponse("Failed..")

    return render(request,'buynow.html',{'x':x})

def buyfunction(request,id):
    x = productmodel.objects.get(id=id)

    if request.method=='POST':
        x.price = request.POST.get('price')

        a=buyform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['uname']
            ph=a.cleaned_data['phone']
            ad=a.cleaned_data['address']
            pr=a.cleaned_data['price']
            mm=a.cleaned_data['mode']
            # o1=request.POST.get('option1')
            # if o1=='on':
            #     o1=True
            # else:
            #     o1=False
            # o2 = request.POST.get('option2')
            # if o2 == 'on':
            #     o2 = True
            # else:
            #     o2 = False
            # o3 = request.POST.get('option3')
            # if o3 == 'on':
            #     o3 = True
            # else:
            #     o3 = False

            b=buy(uname=un,phone=ph,price=pr,address=ad,mode=mm,uid=request.session['id'])
            b.save()
            return redirect(confirm)
        else:
            return HttpResponse("Failed.....")
    return render(request,'buynow.html',{'x':x})

def order(request):
    return render(request,'order.html')
def alreadyuser(request):
    return render(request,'alreadyuser.html')
def alreadyproduct(request):
    return render(request,'alreadyproduct.html')

def alreadycart(request):
    return render(request,'alreadycart.html')

def checkemail(request):
    return render(request,'checkemail.html')
def loginfailed(request):
    return render(request,'loginfailed.html')
def checkerror(request):
    return render(request,'checkerror.html')


def changed(request):
    return render(request,'changedpass.html')

def useredit(request,id):
    a=regmodel.objects.get(id=id)
    # img=str(a.file).split('/')[-1]
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.lname = request.POST.get('lname')
        a.uname=request.POST.get('uname')
        a.email = request.POST.get('email')
        a.address = request.POST.get('address')
        a.phone = request.POST.get('phone')

        # # image
        # if len(request.FILES)!=0:#new file checking
        #     if len(a.file)!=0:#old file checking
        #         os.remove(a.file.path)#remove old file using os
        #     a.file=request.FILES['file']
        a.save()
        return redirect(profile)

    return render(request,'useredit.html',{'a':a})


def bill(request):
    a=buy.objects.all()
    if request.method=='POST':
        pp=request.session['price']
        qt=request.session['quantity']
        a.pp*=a.qt
        a.save()

    return render(request,'bill.html',{'a':a})

def confirm(request):

    return render(request,'confirm.html')


def displaybill(request):
    p=buy.objects.all()
    # x = addamount.objects.all()
    id = request.session['id']
    return render(request,'billdisp.html',{'p':p,'id':id})


