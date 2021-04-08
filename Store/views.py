from django.shortcuts import render
from Store.models import products
from django.views.generic import ListView
from .filter import StoreFilter
from django.shortcuts import render,redirect
import os
from django.http import HttpResponse
from django.conf import settings
from Account.models import Profile
from django.contrib import messages
from gallery.models import movies, behind_the_scene
from django.contrib.auth.decorators import login_required
# Create your views here.


class ProductPreview(ListView):
    #raise_exception = False
    redirect_field_name = 'redirect_to'
    model = products
    template_name = 'index.html'
    context_object_name = 'products'
    ordering = ['-title']

    def get_context_data(self, **kwargs):
        data = super(ProductPreview, self).get_context_data(**kwargs)
        try:
            movie = movies.objects.all().order_by('-date')[:4]
            data['movies'] = movie
        except AttributeError:
            pass

        try:
            scene = behind_the_scene.objects.all().order_by('-date')[:4]
            data['scenes'] = scene

        except AttributeError:
            pass
        data['products'] = products.objects.all().order_by('-date')[:3]
        data['Filter'] = StoreFilter(self.request.GET,queryset=data['products'])
        data['products'] = data['Filter'].qs
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user = self.request.user)
            data['profile'] = profile
        return data

    def get_queryset(self):
        try:
            noti  = products.objects.last()
            noti = noti.title
            messages.success(self.request,"The" + "'" + str(noti) + "'" + "File was the most recently added one, check it out!")

        except AttributeError:
            pass

        queryset = {'products': products.objects.all()}
        return queryset




class ProductView(ListView):
    redirect_field_name = 'redirect_to'
    model = products
    template_name = 'ProductView.html'
    context_object_name = 'products'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        data = super(ProductView, self).get_context_data(**kwargs)
        data['user'] = self.request.user
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user = self.request.user)
            data['profile'] = profile
        try:
            product= products.objects.all()
            data['products'] = product
        except AttributeError:
            pass
        data['Filter'] = StoreFilter(self.request.GET,queryset=data['products'])
        data['products'] = data['Filter'].qs

        return data

    def get_queryset(self):
        queryset = {'products': products.objects.all()}
        return queryset