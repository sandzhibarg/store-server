from typing import Any, Dict
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from products.models import ProductCategory, Product, Basket
from users.models import User

# Create your views here.
# создание функций/представлений/контроллеров для отображения наших шаблонов
class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context
    
class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data() # определяем наш класс
        context['title'] = 'Store - Каталог' # переопределяем поля в контексте
        context['categories'] = ProductCategory.objects.all() #
        return context


# def products(request, category_id=None, page_number=1):
#     # используем тернарный оператор (также можем сразу передать в context)
#     products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
    
#     per_page = 3
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)

#     context = {
#         'title': 'Store - Каталог',
#         'products': products_paginator,
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER']) # возвращаем на ту же страницу где было выполнено действие

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

