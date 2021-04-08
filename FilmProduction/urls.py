"""FilmProduction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Account.views import account_create_view,account_view,CustomLoginView,logout_view,AuthView
from Store.views import ProductPreview,ProductView
from Payment.views import stripe_config,  create_checkout_session, success, cancel, stripe_webhook, subView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', account_create_view),
    path('accounts/profile/', account_view),
    path('login/', AuthView),
    path('logout/', logout_view),
    path('', ProductPreview.as_view()),
    path('product/', ProductView.as_view()),
    path('config/', stripe_config),
    path('create-checkout-session/<int:id>/', create_checkout_session),
    path('success/', success),  # new
    path('cancel/', cancel),
    path('webhook/', stripe_webhook),
    path('subscription/', subView),
    path('webhook/', stripe_webhook),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
