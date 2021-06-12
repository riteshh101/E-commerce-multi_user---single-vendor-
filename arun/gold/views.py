from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import RegistrationForm,LoginForm,ChangePass
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

########################################### ABOUT PAGE FUNCTION HERE ######################################################
def about(request):
    return render(request, 'about.html')
#############################################ABOUT FUNCTION FINISHED HERE ###############################################


########################################## LOGOUT FUNCTION HERE ################################################################

def user_logout(request):
    logout(request)
    return redirect('/login')
###############################################LOGOUT FINISHED HERE #########################################################


######################################################CONTACT FUNCTION HERE  ########################################################

def contact(request):
    if request.POST:
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message = request.POST['message']
        obj = Contact(name=name, email=email, message=message, mobile=mobile)
        obj.save()
        messages.info(request,'Feedback submited sucessfully')
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

################################################## CONTACT FUNCTION END HERE ########################################################

######################################################  HOME PAGE FUNCTION HERE ####################################
def home(request):
    product = Product.objects.all()
    pic = slider.objects.all()
    rang = len(pic)
    c = range(1, rang)
    #param = {'range': c, 'image': pic, 'product': product}
    return render(request, "home.html",{'range': c, 'image': pic, 'product': product})
##########################################################HOME PAGE END HERE ##########################################


############################################# SLIDER IMAGE FUNCTION HERE ##############################################

def show(request):
    image = slider.objects.all()
    return render(request, "show2.html", {'image': image})

############################################SLIDER FUNCTION FINISHED HERE #############################################

############################################ PRODUCT FULL DETAIL PAGE HERE###############################################

def buy(request,id):
    x=Product.objects.filter(id=id)
    cmt=comment.objects.filter(idd=id)
    return render(request, 'buy.html', {'product': x, 'cmt': cmt})

############################################# PRODUCT FULL DETAIL FINISHED HERE ##############################################

################################################  SEARCH SYSTEM HERE  #######################################################

def search(request):
    if request.method=="POST":
        srch = request.POST['category']
        if srch:
            match = Product.objects.filter(product_name=srch)
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'no result found...........................')
        else:
            return redirect('/')
    return render(request,'search.html')

##################################################  SEARCH SYSTEM FINISHED HERE ##############################################

##################################################### REGISTRATION SYSTEM HERE ################################################

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'You are successfully Registered Thank You!!....')
            form.save()
            form = RegistrationForm()
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})

######################################################REGISTRATION FINISHED HERE ##############################################


####################################################  LOGIN SYSTEM HERE ##########################################################

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pw = form.cleaned_data['password']
                user = authenticate(username=uname,password=pw)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            form = LoginForm()
        return render(request, 'login.html',{'form':form})
    else:
        return redirect('/')

################################################  LOGIN SYSTEM END HERE  ##########################################################


##############################################all function here cart realated#######################################################
#cart Update
def user_cart(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            user = request.user.username
            pro = Product.objects.get(id=id)
            crtmatch = cart.objects.filter(username=user)
            c=[]
            for x in crtmatch:
                c.append(x.idd)

            if id in c:
                carts = cart.objects.filter(username=request.user).get(idd=id)
                carts.count = carts.count + 1
                carts.final_price = carts.count*carts.price
                print(carts.final_price)
                carts.save()
                return redirect('/cart')

            else:
                count=1
                ct = cart(product_name=pro.product_name,username=user,price=pro.price,image=pro.image,idd=pro.id,count=count,final_price=pro.price)
                ct.save()
                return redirect('/cart')
# main cart.html page
def cart_page(request):
    if request.user.is_authenticated:
        user =request.user.username
        ct=cart.objects.filter(username=user)
        money = 0
        for x in ct:
            money = money+x.final_price
        rang = len(ct)
        c = range(1, rang+1)
    return render(request,'cart.html',{'pro':ct,'mn':money,'rng':c})

def cart_remove(request,id):
    if request.user.is_authenticated:
        if request.method =="POST":
            ct =cart.objects.get(pk=id)
            ct.delete()
            return redirect('/cart')
def cart_plus(request,id):
    if request.user.is_authenticated:
        carts = cart.objects.filter(username=request.user).get(idd=id)
        carts.count = carts.count+1
        carts.final_price = carts.count * carts.price
        carts.save()
        return redirect('/cart')

def cart_minus(request,id):
    if request.user.is_authenticated:
        carts = cart.objects.filter(username=request.user).get(idd=id)
        if  carts.count != 1:
            carts.count = carts.count - 1
            carts.final_price = carts.count * carts.price
            carts.save()
            return redirect('/cart')
        else:
            return redirect('/cart')
########################################################## CART FUNCTION FINISHED HERE ####################################################################################

###########################################################CHANGE PASSOWRD FROM OLD PASSWORD FUNCTION####################################

def change_password(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            fm =ChangePass(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)#by this user not logout after changepassword. if we not use this user forcefully logout.
                messages.success(request,'Password change successfully Thank You!!!!!!')
                return redirect('/changepass')
        else:
            fm = ChangePass(user=request.user)
        return render(request,'changepass.html',{'fm':fm})
    else:
        return redirect('/login')

#################################################After Click Buy button Function##################################################

def buypage(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            username=request.user.username
            name=request.POST['name']
            email=request.POST['email']
            address1=request.POST['address1']
            mobile=request.POST['mobile']
            city=request.POST['city']
            state=request.POST['state']
            zip=request.POST['zip']
            cd=str(mobile)
            cdd=len(cd)
            if cdd ==10:
                ct=user_address(username=username,name=name,email=email,address1=address1,mobile=mobile,city=city,state=state,zip=zip)
                ct.save()
                messages.success(request,'Your Address Add Successfully......')
                return redirect('/buypage')
            else:
                messages.error(request,'Please fill valid mobile number....')
                return redirect('/buypage')
        else:
            ct=user_address.objects.filter(username=request.user)
            return render(request,'buypage.html',{'ct':ct})
    else:
        return redirect('/login')

##############################################User Address Page Function Finished Here#########################################

########################################ADRESS REMOVE HERE#################################################################

def remove_address(request,id):
    if request.user.is_authenticated:
        ct = user_address.objects.get(pk=id)
        ct.delete()
        return redirect('/buypage')
    else:
        return redirect('/login')
##########################################Remove Address Finished Here#################################################

############################################### Order Detail Here ################################################

def order_detail(request,id):
    if request.user.is_authenticated:
        ct=cart.objects.filter(username=request.user.username)
        money = 0
        for x in ct:
            money = money + x.final_price
        ctt = user_address.objects.filter(id=id)
        return render(request,'order_detail.html',{'ct':ct,'mn':money,'ctt':ctt})
    else:
        return redirect('/login')
##################################################Order Detail Finished Here#########################################

#############################################  pdf_detail page rander here  ##############################################

def pdf_detail(request):
    return render(request,'pdf_detail.html')

############################################### Comment Function here ###########################################

def user_comment(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            cmt=request.POST['cmt']
            ct=comment(idd=id,uname=request.user.username, desc=cmt)
            ct.save()
            print("yha tk code chal rha")
            return redirect(request,'/buy/'+str(id))
    else:
        messages.error(request,'For Comment First you need to Login...')
        return redirect('/login')