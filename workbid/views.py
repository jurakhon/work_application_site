from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

class UserListView(ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "user_list"

class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
    context_object_name = "user_detail"

class UserCreateView(CreateView):
    model = User
    template_name = "user_create.html"
    fields = ["name", "surname", "email", "phone_number", "username", "password", "is_active"]
    context_object_name = "user_create"
    success_url = reverse_lazy("user_list")

class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    context_object_name = "user_update"
    success_url = reverse_lazy("user_list")

class UserDeleteView(DeleteView):
    model = User
    template_name = "confirm_delete.html"
    context_object_name = "user_delete"
    success_url = reverse_lazy("user_list")

class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "category_list"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_detail.html"
    context_object_name = "category_detail"

class CategoryCreateView(CreateView):
    model = Category
    fields = ["name", "image"]
    template_name = "category_create.html"
    context_object_name = "category_create"
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name", "image"]
    context_object_name = "category_update"
    template_name = "category_update.html"
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(DeleteView):
    model = Category
    context_object_name = "category_delete"
    success_url = reverse_lazy("category_list")
    template_name = "confirm_delete.html"

class JobListView(ListView):
    model = Job
    context_object_name = "job_list"
    template_name = "job_list.html"

class JobDetailView(DetailView):
    model = Job
    context_object_name = "job_detail"
    template_name = "job_detail.html"

class JobCreateView(CreateView):
    model = Job
    fields = ["title", "description", "image", "video","category","user","location","is_active"]
    context_object_name = "job_create"
    template_name = "job_create.html"
    success_url = reverse_lazy("job_list")

class JobUpdateView(UpdateView):
    model = Job
    fields = ["title", "description", "image", "video","category","user","location","is_active"]
    context_object_name = "job_update"
    success_url = reverse_lazy("job_list")
    template_name = "job_update.html"

class JobDeleteView(DeleteView):
    model = Job
    context_object_name = "job_delete"
    success_url = reverse_lazy("job_list")
    template_name = "confirm_delete.html"

class BidderListView(ListView):
    model = Bidder
    context_object_name = "bidder_list"
    template_name = "bidder_list.html"

class BidderDetailView(DetailView):
    model = Bidder
    context_object_name = "bidder_detail"
    template_name = "bidder_detail.html"

class BidderCreateView(CreateView):
    model = Bidder
    fields = ["user", "message", "bid_amount", "duration", "status"]
    context_object_name = "bidder_create"
    template_name = "bidder_create.html"
    success_url = reverse_lazy("bidder_list")

class BidderUpdateView(UpdateView):
    model = Bidder
    fields = ["user", "message", "bid_amount", "duration", "status"]
    context_object_name = "bidder_update"
    template_name = "bidder_update.html"
    success_url = reverse_lazy("bidder_list")

class BidderDeleteView(DeleteView):
    model = Bidder
    context_object_name = "bidder_delete"
    success_url = reverse_lazy("bidder_list")
    template_name = "confirm_delete.html"







