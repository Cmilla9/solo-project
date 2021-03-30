from django.shortcuts import render, redirect
from .models import User, UserManager, BusinessUser, BusinessUserManager
from django.contrib import messages
# from django.db.models import Q
import bcrypt

def index(request):
    if request.method == "GET":
        businessusers = BusinessUser.objects.all()
        context = {
            'businessusers': businessusers,
        }
        return render(request,'index.html', context)
    else:
        user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])
        if not user:  
            return redirect('/')
        user = User.objects.get(id = request.session['user_id'])
        businessusers = BusinessUser.objects.all()
        context = {
            'businessusers': businessusers,
            'user': user,
        }
        return render(request, 'index.html', context)

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = pw_hash,
            )
            messages.success(request, "You have successfully registered!")
            return redirect('/register')

def sign_in(request):
    if request.method == "GET":
        return render(request, 'sign_in.html')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if len(user) > 0:
            if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                request.session['user_id'] = user[0].id
                return redirect('/')
            else:
                messages.error(request, "Incorrect Password.")
                return redirect('/login')
        else:
            messages.error(request, "This email hasn't been registered.")
            return redirect('/login')

def register_business(request):
    if request.method == "GET":
        return render(request, 'register_business.html')
    else:
        errors = BusinessUser.objects.business_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            BusinessUser.objects.create(
                business_name = request.POST['business_name'],
                description = request.POST['description'],
                email = request.POST['email'],
                food_category = request.POST['food_category'],
                phone_number = request.POST['phone_number'],
                password = pw_hash,
            )
            messages.success(request, "You have successfully registered!")
            return redirect('/register_business')

def business_login(request):
    if request.method == "GET":
        return render(request, 'sign_in.html')
    else:
        businessuser = BusinessUser.objects.filter(email=request.POST['email'])
        if len(businessuser) > 0:
            if bcrypt.checkpw(request.POST['password'].encode(), businessuser[0].password.encode()):
                request.session['businessuser_id'] = businessuser[0].id
                return redirect(f'/business_profile/{businessuser[0].id}')
            else:
                messages.error(request, "Incorrect Password.")
                return redirect('/login')
        else:
            messages.error(request, "This email hasn't been registered.")
            return redirect('/login')

def logout(request):
    request.session.clear()
    return redirect('/')

# def search(request):
#     user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])
#     if not user:  
#         return redirect('/')
#     user = User.objects.get(id = request.session['user_id'])
#     context = {
#         'user': user,
#     }
#     return render(request, 'search.html', context)

def business_profile(request, businessuser_id):
    # businessuser = None if 'businessuser_id' not in request.session else BusinessUser.objects.get(id=request.session['businessuser_id'])
    # if not businessuser:
    #     return redirect(f'/business_profile/{businessuser_id}')
    businessuser = BusinessUser.objects.get(id=f'{businessuser_id}')
    context = {
        'businessuser': businessuser
    }
    return render(request, 'business_profile.html', context)

def update_business(request, businessuser_id):
    businessuser = None if 'businessuser_id' not in request.session else BusinessUser.objects.get(id=request.session['businessuser_id'])
    if not businessuser:
        return redirect('/')
    if request.method == "POST":
        errors = BusinessUser.objects.business_update(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect(f'/business_profile/{businessuser_id}')
        else:
            businessuser = BusinessUser.objects.get(id=businessuser_id)
            businessuser.business_name = request.POST['business_name']
            businessuser.description = request.POST['description']
            businessuser.current_location = request.POST['current_location']
            businessuser.email = request.POST['email']
            businessuser.phone_number = request.POST['phone_number']
            businessuser.food_category = request.POST['food_category']
            businessuser.save()
            return redirect(f'/business_profile/{businessuser.id}')

def searchfood(request):
    print('in main app')
    if request.method == 'POST':
        query= request.POST['q']

        # submitbutton= request.GET.get('submit')
        print(query)
        if query is not None:
            # lookups= Q(food_category__icontains=query)

            # results= BusinessUser.objects.filter(lookups).distinct()
            results= BusinessUser.objects.filter(food_category=query)
            print(results)
            context={
                'results': results
                }
            return render(request,'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
