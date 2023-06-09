from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):

    if request.method == 'GET':
        return render(request,'signup.html',{'form':UserCreationForm})
        #print('sending form')
        
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                return HttpResponse('User created')
            except:
                return HttpResponse('User already exists')

        return HttpResponse('Passwords do not match')
        #print(request.POST)
        #print('processing form')


    #form = UserCreationForm()
    