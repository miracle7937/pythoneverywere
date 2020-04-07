from django.shortcuts import render,  redirect
from Authentication.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Registration
from .filters import PatientFilter
from django.contrib.auth.decorators import login_required
from .decorator import allowed_users
from django.contrib.auth.models import Group




# Create your views here.
def medSignUp(request):
    print(request.POST)
    if request.user.is_authenticated:
        return redirect('statics')
    else:
        form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(request.POST)
            user = form.save()
            group = Group.objects.get(name='staff')

            user.groups.add(group)
            print(form.cleaned_data.get('email'))
            username = form.cleaned_data.get('username')
            messages.success(request, 'account created successful ' + username)
            return redirect("user-login")

    context = {
        'form': form
    }
    return render(request, 'signUpMed.html', context)


@login_required(login_url='user-login')
def patientForm(request):
    print(request.POST)
    if request.method == 'POST':
        patientName = request.POST.get('patientName')
        patientNumber = request.POST.get('patientNumber')
        patientAddress = request.POST.get('patientAddress')
        patientcity = request.POST.get('patientcity')
        patientSex = request.POST.get('patientSex')
        patientDOB = request.POST.get('patientDOB')
        careNumber = request.POST.get('careNumber')
        MaritalStatus = request.POST.get('MaritalStatus')
        RegistrationLocation = request.POST.get('RegistrationLocation')
        sickness = request.POST.get('sickness')
        doctorName = request.POST.get('doctorName')
        registerion = Registration.objects.create( patientName=patientName, patientNumber=patientNumber,patientAddress=patientAddress,
        sickness = sickness,
        
        patientcity=patientcity,patientSex = patientSex, patientDOB= patientDOB, careNumber= careNumber,
        MaritalStatus = MaritalStatus, RegistrationLocation =RegistrationLocation, doctorName=doctorName)

        registerion.save()
        messages.success(request, 'Record created successful ')

        return redirect('statics')

    
    print(request.POST)


    return render(request, 'patient-form.html')


@login_required(login_url='user-login')
def statics(request):
    obj = Registration.objects
    
    mal= obj.filter(sickness='Malaria').count()
    cov = obj.filter(sickness='Covid 19').count()
    typ = obj.filter(sickness='Typhoid fever').count()
    stone = obj.filter(sickness='Kidney Stone').count()
    tooth = obj.filter(sickness='Tooth Decay').count()
    context={
        'mal': mal,
        'cov':cov,
        'typ':typ,
        'stone':stone,
        'tooth': tooth
    }
    
    return render(request, 'chartPage.html',context)



@allowed_users(allowed_roles=['staff'])
def admin(request):
    patients = Registration.objects.all()
    print(patients)
    myFilter = PatientFilter(request.GET, queryset=patients)
    patients= myFilter.qs
    context= {
        'patients':patients,
        'myFilter': myFilter
        
    }
    return render(request, 'user-table.html', context)









def loginPage(request):
    print(request.POST)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            print('this is authenticated ', user)

            if user is not None:
                login(request, user)
                return redirect('statics')

            else:
                messages.info(request, 'email or password is not correct')
        except:
            messages.info(request, "user doesn't exist ")

    return render(request, 'sign_in.html')



def signUp(request):
    print(request.POST)
    if request.user.is_authenticated:
        return redirect('statics')
    else:
        form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        print(form.errors)
        if form.is_valid():
            form.is_staff =True
            user = form.save()
            group = Group.objects.get(name='patient')

            user.groups.add(group)
            print(form.cleaned_data.get('email'))
            username = form.cleaned_data.get('username')
            messages.success(request, 'account created successful ' + username)
            return redirect("user-login")

    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context)


@login_required(login_url='user-login')
def logoutUser(request):

    logout(request=request)
    return redirect('user-login')





def base(request):
    return render(request,'base.html',)


    
