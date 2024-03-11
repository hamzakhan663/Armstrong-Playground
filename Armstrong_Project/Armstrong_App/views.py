from django.shortcuts import render, redirect
from .forms import ArmstrongUserProfileForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from .models import ArmstrongUserProfile, UserAttempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count


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
                raise ValueError("Invalid username or password")
                
                
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
        form = ArmstrongUserProfileForm(request.POST)
        
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
        form = ArmstrongUserProfileForm(request.POST)
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


@login_required
def search(request):
    if request.method == 'POST':
        input_type = request.POST.get('inputType')

        if input_type == 'range':
            min_number = int(request.POST.get('minNumber', 0))
            max_number = int(request.POST.get('maxNumber', 0))
            
            if not (min_number and max_number):
                raise ValueError("Please provide both minimum and maximum numbers.")

            armstrong_numbers = [n for n in range(min_number, max_number + 1) if is_armstrong_number(n)]

            result = {
                'armstrong_numbers': armstrong_numbers,
                'total_count': len(armstrong_numbers),
                'input_type': input_type,
                'attempt_value': f'{min_number}-{max_number}',
                'formatted_result': f'Found {len(armstrong_numbers)} Armstrong numbers in the range {min_number}-{max_number}.',
            }
        elif input_type == 'single':
            single_number = int(request.POST.get('singleNumber', 0))
            
            if not (single_number):
                raise ValueError("Please provide a number.")

            result = {
                'single_number': single_number,
                'is_armstrong': is_armstrong_number(single_number),
                'input_type': input_type,
                'attempt_value': str(single_number),
                'formatted_result': f'The number {single_number} {"is" if is_armstrong_number(single_number) else "is not"} an Armstrong number.'
            }
        else:
            result = {'error': 'Invalid input type'}
            
        UserAttempt.objects.create(
            user=request.user,  # Assuming you have a user associated with the request
            attempt_type=input_type,
            attempt_value=result['attempt_value'],
            result=result['formatted_result'],
        )

        return render(request, 'Armstrong_App/search.html', {'result': result})

    return render(request, 'Armstrong_App/search.html', {'result': None})


def is_armstrong_number(number):
    num_str = str(number)
    n = len(num_str)
    armstrong_sum = sum(int(digit) ** n for digit in num_str)
    return armstrong_sum == number

@login_required
def show_attempts(request):
    user_attempts = UserAttempt.objects.filter(user=request.user).order_by('-timestamp')
       
    return render(request, 'Armstrong_App/show_attempts.html', {'user_attempts': user_attempts})































































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
