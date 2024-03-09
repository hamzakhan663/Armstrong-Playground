from django.shortcuts import render, redirect
from .forms import ArmstrongUserProfileForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from .models import ArmstrongUserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

def home(request):
    return render(request,'Armstrong_App/home.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = RegisterForm()
    return render(request, 'Armstrong_App/register.html',{'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            
            user = authenticate(username=username, password=password)
            
            if user != None:
                login(request, user)
                return redirect('home')
                
    else:
        form = LoginForm()
        return render(request, 'Armstrong_App/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

def update_profile(request):
    user_obj = User.objects.get(id=request.user.id)

    profile = ArmstrongUserProfile.objects.filter(user=user_obj)
    
    if len(profile) > 0:
        profile = profile[0]
    else:
        profile = None
    
    if request.method == 'POST':
        form = ArmstrongUserProfileForm(request.POST, instance=profile)
        
    else:
        form = ArmstrongUserProfileForm()
        context = {
        'profile':profile,
        'form': form,
        }
        return render(request, 'Armstrong_App/update_profile.html',context)



def create_profile(request):
    user_obj = User.objects.get(id=request.user.id)

    profile = ArmstrongUserProfile.objects.filter(user=user_obj)
    
    if len(profile) > 0:
        profile = profile[0]
    else:
        profile = None

    if request.method == 'POST':
        print("========")
        form = ArmstrongUserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            print("======+++++++++==")
            name = request.POST.get('name', '')
            contact_number = request.POST.get('contact_number', '')
            user = User.objects.get(id=request.user.id)

            armstrong_user_profile = ArmstrongUserProfile(user=user,name=name,contact_number=contact_number)
            armstrong_user_profile.save()
            return redirect('home')
    else:
        form = ArmstrongUserProfileForm()
        context = {
        'profile':profile,
        'form': form,
        }
        return render(request, 'Armstrong_App/create_profile.html',context)


def delete_profile(request):
    user_obj = User.objects.get(id=request.user.id)

    try:
        profile = ArmstrongUserProfile.objects.get(user=user_obj)
    except ArmstrongUserProfile.DoesNotExist:
        # Handle the case where the user profile does not exist
        profile = None

    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    else:
        context = {'profile': profile}
        return render(request, 'Armstrong_App/delete_profile.html', context)



def search(request):
    if request.method == 'POST':
        input_type = request.POST.get('inputType')

        if input_type == 'range':
            min_number = int(request.POST.get('minNumber', 0))
            max_number = int(request.POST.get('maxNumber', 0))

            armstrong_numbers = [n for n in range(min_number, max_number + 1) if is_armstrong_number(n)]

            result = {
                'armstrong_numbers': armstrong_numbers,
                'total_count': len(armstrong_numbers),
                'input_type': input_type
            }
        elif input_type == 'single':
            single_number = int(request.POST.get('singleNumber', 0))

            result = {
                'single_number': single_number,
                'is_armstrong': is_armstrong_number(single_number),
                'input_type': input_type
            }
        else:
            result = {'error': 'Invalid input type'}

        return render(request, 'Armstrong_App/search.html', {'result': result})

    return render(request, 'Armstrong_App/search.html', {'result': None})


def is_armstrong_number(number):
    num_str = str(number)
    n = len(num_str)
    armstrong_sum = sum(int(digit) ** n for digit in num_str)
    return armstrong_sum == number




































































# def register(request):
    
#     if request.method == 'POST':
#         form = ArmstrongUserForm(request.POST)
#         if form.is_valid():
#             name = request.POST.get('name', '')
#             email = request.POST.get('email', '')
#             contact_number = request.POST.get('contact_number', '')
#             username = request.POST.get('username', '')
#             password = request.POST.get('password', '')
            
#             user = User.objects.create(username=username, password=password)
#             armstrong_user = ArmstrongUser(user=user, name=name, contact_number=contact_number)
            
#             armstrong_user.save()
#             return redirect('home')
#     else:
#         form = ArmstrongUserForm()
#         return render(request, 'Armstrong_App/register.html',{'form': form})
