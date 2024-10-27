from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from goods.models import Categories, Products
from .cart import Cart

def index(request):
    categories = Categories.objects.all()  # Получаем все категории

    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
        'categories': categories,  # Добавляем категории в контекст
    }

    return render(request, 'myapp/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': (
            "Мы - команда профессионалов, специализирующихся на продаже мебели, "
            "предлагающая широкий ассортимент товаров для вашего дома и офиса. "
            "Наши специалисты с радостью помогут вам выбрать идеальные решения, "
            "которые сочетат стиль, комфорт и функциональность. "
            "Мы стремимся к качеству и заботимся о каждом клиенте, "
            "предоставляя только лучшие материалы и современные технологии. "
            "С нами вы найдете мебель, которая не только украсит ваше пространство, "
            "но и станет отражением вашего уникального стиля."
        )
    }

    return render(request, 'myapp/about.html', context)


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)

    quantity = int(request.POST.get('quantity', 1))  # Получаем количество из формы
    cart.add(product, quantity)  # Добавляем продукт в корзину с указанным количеством
    return redirect('myapp:cart_detail')  # Перенаправляем на страницу корзины


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)  # Удаляем продукт из корзины
    return redirect('myapp:cart_detail')  # Перенаправляем на страницу корзины

def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart,  # Передаем корзину в контекст
    }
    return render(request, 'myapp/cart/detail.html', context)  # Убедитесь, что путь к шаблону правильный

