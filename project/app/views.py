from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'home.html' )
def register(request):
    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        print("hii")

        name=request.COOKIES.get['name']
        print(name)
        
    else:
        return render(request, 'login.html')


def registerdata(request):
    print(request.method)
    print(request.POST)
    cstoken = request.POST.get('csrfmiddlewaretoken')
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')
    #print(cstoken)
    #print(name)
    #print(email)
    #print(contact)
    #print(password)
    # response = render(request,'login.html')
    # response.set_cookie('name',name)
    # response.set_cookie('contact',contact)
    # response.set_cookie('email', email)
    # response.set_cookie('password', password)
    # return response
      
def login(request):
    if request.method =='POST':
      email= request.POST.get('email')
      password=request.POST.get('password')

      print(email)

    name= request.COOKIES['name']
    email1= request.COOKIES['email']
    contact= request.COOKIES['contact']
    password1= request.COOKIES['password']
    print(name,email,contact,password)

     # if email1==email:

      #   if password1==password:
       #     data={ 'n1':name,
        #           'n2':email,
        #           'n3':contact,
         #          'n4':password}
            
       #  else:
     #       msg="msg&password not matched" 


      #else:
       #  msg='email id not registed'
   # else:
  #      return render(request,'login.html')


# def delete(request):
#     response = render(request,'home.html')
#     response.delete_cookie('name')
#     response.delete_cookie('contact')
#     response.delete_cookie('email')
#     response.delete_cookie('password')
#     return response


def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        
        data={'name':name,
              'email':email,
              'contact':contact,
              'password':password}

        request.session['data']=data
        return render(request,'login.html')
    else:
     return render(request,'register.html')  
    

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        data123=request.session.get('data')
        print(data123)

    else:
        return render(request,'login.html')