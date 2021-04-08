from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import logout
from .models import Profile
import stripe
from django.conf import settings
from django.contrib.auth import authenticate,login
# Create your views here.

class CustomLoginView(LoginView):
    template_name = "login/login_try.html"  # your template
    from_class = LoginForm,RegistrationForm
    redirect_authenticated_user = True
    extra_context = {'registration':RegistrationForm}

def AuthView(request):
    register = RegistrationForm(request.POST or None)
    form = LoginForm()

    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            print('signin')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.success(request,'Incorrect user or password, please try again')
                LoginForm()

        elif request.POST.get('submit') == 'sign_up':
            print('signup')
            if register.is_valid():
                messages.success(request, 'Sucessful registration, please now sign in')
                user = register.save()
                Profile.objects.create(
                    user = user
            )
                return redirect('/accounts/profile/')
            else:
                messages.success(request, 'Unsucessful signup please try again')
                RegistrationForm()







    # register = RegistrationForm(request.POST or None)
    # print(LoginForm)
    # if register.is_valid():
    #     user = register.save()
    #
    #     Profile.objects.create(
    #         user = user
    #     )
    #
    #     return redirect('/accounts/profile/')
    #
    # else:
    #     register = RegistrationForm()


    return render(request,"login/login_try.html",{'form':form,'register':register})




def account_create_view(request):
    registration = RegistrationForm(request.POST or None)


    if registration.is_valid():
        user = registration.save()

        Profile.objects.create(
            user = user
        )


        return redirect('/accounts/profile/')

    else:
        print(registration.errors)

    return render(request, "registration/register.html",{'registration':registration})


def account_view(request):
    if request.user.is_authenticated:
        customer = Profile.objects.get(user = request.user)
        if customer.paid == True:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            subscription = stripe.Subscription.retrieve(customer.stripeSubscriptionId)
            product = stripe.Product.retrieve(subscription.plan.product)
            return render(request, "account/account.html", {'user': request.user,
                                                            'subscription': subscription,
                                                            'product': product})

        return render(request, "account/account.html", {"user": request.user})

    return redirect("/login/")




def logout_view(request):
    logout(request)
    return redirect('/')




