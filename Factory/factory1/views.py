from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class ProductListView(ListView):
    model = TwixProduct
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = TwixProduct
    template_name = 'product_detail.html'
    context_object_name = 'product'