from django.urls import path
from myapp import views  # Импортируем представления из приложения myapp

app_name = 'myapp'  # Устанавливаем пространство имен для маршрутов

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница 'О нас'
    path('cart/', views.cart_detail, name='cart_detail'),  # Страница корзины
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),  # Добавить товар в корзину
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]

