from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from signup.models import student
# Create your views here.
def signup(request):
    return render(request,'signup.html')
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
       
        # course=request.POST['course']
        img=request.FILES.get('file')
             
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                
                students=student( First_Name=first_name,
                                      Last_Name=last_name, 
                                      User_Name=username,
                                      Email=email,
                                     
                                       image=img)
               
                students.save()
              
                
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup') 
        messages.info(request, f'Welcome {username}.SuccessFully completed.......')  
        return redirect('msgpage')
    else:
        return render(request,'signup.html')
def msgpage(request):
    
    return render(request,'notification.html')  