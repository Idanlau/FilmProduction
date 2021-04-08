import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # new
from django.http.response import JsonResponse, HttpResponse  # updated
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from Account.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
import json


# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)



@csrf_exempt
def create_checkout_session(request,id):
    if id == 1:
        price = settings.MONTH_PRICE_ID
    elif id == 2:
        price = settings.BIANUAL_PRICE_ID
    elif id ==3:
        price = settings.ANUAL_PRICE_ID
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url= domain_url,
                cancel_url=domain_url + 'subscription/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price':price,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@login_required
def success(request):
    return render(request, 'sucess.html')


@login_required
def cancel(request):
    return render(request, 'cancel.html')

@login_required
def subView(request):
    customer = request.user.Profile
    print(customer.paid)
    if request.user.is_authenticated and customer.paid == False:
        return render(request, 'pay.html')

    else:
        return redirect("/accounts/profile/")




@csrf_exempt
def stripe_webhook(request):
    print('running webhook')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Works!!!")
        session = event['data']['object']
        print(session)

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        customer = Profile.objects.get(user = user)
        customer.stripeCustomerId = stripe_customer_id
        customer.stripeSubscriptionId = stripe_subscription_id
        customer.paid = True
        customer.save()

    return HttpResponse(status=200)

