from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, 'index.html')


def subscribe(request):
    if request.method =='POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email= request.POST['email']

        if password1==password2: 
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('subscribe')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('subscribe')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            return redirect('/')
    else:
        return render(request, 'subscribe.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# def cart(request):
#     cart_items = CartItem.objects.all()
#     return render(request, 'cart.html', {'cart_items': cart_items})

# def add_to_cart(request, product_id):
#     product = get_object_or_404(Food, pk=product_id)
#     cart_item, created = CartItem.objects.get_or_create(product=product)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('cart')