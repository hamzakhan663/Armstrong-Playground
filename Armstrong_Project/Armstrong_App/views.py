from django.shortcuts import render, redirect
from .forms import ArmstrongUserProfileForm, RegisterForm
from django.contrib.auth.models import User
from .models import ArmstrongUserProfile

# Create your views here.
def home(request):
    armstrong_user = User.objects.get(id=request.user.id)
    
    return render(request,'Armstrong_App/home.html',{'armstrong_user':armstrong_user})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = RegisterForm()
    return render(request, 'Armstrong_App/register.html',{'form': form})


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
    
    if request.method == 'POST':
        user_obj = User.objects.get(id=request.user.id)

        profile = ArmstrongUserProfile.objects.filter(user=user_obj)
        profile = profile[0]
        
        profile.delete()
        return redirect('home')
    else:
        user_obj = User.objects.get(id=request.user.id)

        profile = ArmstrongUserProfile.objects.get(user=user_obj)
        context = {
        'profile':profile
        }
        return render(request, 'Armstrong_App/delete_profile.html', context)





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
