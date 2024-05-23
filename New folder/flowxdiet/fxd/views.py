from ast import main
from email import message
from re import U, sub
from django.contrib import messages
# WHsdIkGtuHaqg4srM6YoyA==ru59arnvytGYDtIN
import email
from multiprocessing import context
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.models import User
from fxd.models import calorie, conta
from fxd.models import conta
from fxd.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"home.html")

def finds(request):
    import json
    import requests
    if request.method =='POST':
        username = request.POST['username']
        batchno = request.POST['batchno']
        foods = request.POST['foods']
        
        if username=='' or batchno== '' or foods== '':
            return render(request, "finds.html")
        
        f=calorie.objects.create(username=username, batchno=batchno, foods=foods)
        f.save()
        
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + foods, headers = {'X-Api-Key':'WHsdIkGtuHaqg4srM6YoyA==ru59arnvytGYDtIN'})
        try:
            api=json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops ! There was an error"
            print(e)
        return render(request,"finds.html",{'api':api})
    else:
        return render(request, "finds.html",{'query':'Enter a valid query'}) 
    # query = '1lb brisket and fries'
    # api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    # response = requests.get(api_url, headers={'X-Api-Key': 'WHsdIkGtuHaqg4srM6YoyA==ru59arnvytGYDtIN'})
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)
    

# def login(request):
#     return render(request,"login.html")

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
    # if request.method =='POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     confirmpassword = request.POST['confirmpassword']
    
    #     if username=='' or password=='' or confirmpassword=='':
    #         context['errmsg']="Fields cannot be Empty"
    #         return render(request, "register.html",context)
        
    #     u=main.objects.create(username=username, password=password, confirmpassword=confirmpassword)
    #     u.save()
    #     messages.success(request,'Registration Successful')
    #     return render(request,"login.html")
    # else:
    #     return render(request,"register.html")
        
        if password==confirmpassword:
            u=User.objects.create_user(username=username,password=confirmpassword)
            u.is_staff=True
            u.is_superuser=True
            u.save()
            messages.success(request,'Registered Successfully.')
            return redirect("login")
        else:
            messages.warning(request,'Password Mismatching..!!!')
            return redirect('register')
    else:
        form=CreateUserForm()
        return render(request, "register.html", {'form':form})
    
    # if request.method =='POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     confirmpassword = request.POST['confirmpassword']
        
    #     if username=='' or password=='' or confirmpassword=='':
    #         context['errmsg']="Fields cannot be Empty"
    #         return render(request, "register.html",context)
        
    #     u=main.objects.create(username=username, password=password, confirmpassword=confirmpassword)
    #     u.save()
    #     messages.success(request,'Registration Successful')
    #     return render(request,"login.html")
    # else:
    #     return render(request,"register.html")
    
# def login(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         if username=='' or password=='':
#             messages.warning(request,'Fields cannot be Empty')
#             return render(request, "register.html",context)
        
#         u=User.objects.create(username=username, password=password)
#         u.set_password(password)
#         u.save()
#         return render(request,"home.html")
#     else:
#         return render(request,"login.html")

# def finds(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         batchno = request.POST['batchno']
#         foods = request.POST['foods']
        
#         if username=='' or batchno== '' or foods== '':
#             return render(request, "finds.html")
        
#         f=calorie.objects.create(username=username, batchno=batchno, foods=foods)
#         f.save()
#         return render(request,"finds.html")
#     else:
#         return render(request,"finds.html")

def contact(request):
    if request.method =='POST':
        fullname = request.POST['name']
        dob = request.POST['dob']
        contactno = request.POST['contactno']
        email = request.POST['email']
        address = request.POST['address']
        region = request.POST['region']
        postalcode = request.POST['postalcode']
        if fullname=='' or dob=='' or contactno=='' or email=='' or address=='' or region=='' or postalcode=='':
            return render(request, "home.html")
        
        c=conta.objects.create(fullname=fullname, dob=dob, contactno=contactno, email=email, address=address, region=region, postalcode=postalcode)
        c.save()
        messages.success(request,'Registered Successfully.')
        return redirect("home")
    else:
        return render(request,"contact.html")   
        
    