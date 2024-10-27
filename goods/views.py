from django.shortcuts import render, redirect, get_object_or_404
from goods.models import Products, Categories
from goods.utils import q_search  # Убедитесь, что эта функция импортируется правильно
from django.core.paginator import Paginator

def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    goods = Products.objects.all()

    # Фильтрация по категории
    if category_slug and category_slug != "all":
        goods = goods.filter(category__slug=category_slug)

    # Поиск по запросу
    if query:
        goods = q_search(query)  # Убедитесь, что q_search работает правильно

    # Фильтрация по скидке
    if on_sale:
        goods = goods.filter(discount__gt=0)

    # Сортировка
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    # Пагинация
    paginator = Paginator(goods, 3)  # 3 товара на страницу
    current_page = paginator.get_page(page)

    # Получение всех категорий
    categories = Categories.objects.all()

    context = {
        "title": "Каталог",
        "goods": current_page,
        "slug_url": category_slug,
        "categories": categories,
    }

    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, 'goods/product.html', context)

