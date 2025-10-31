from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Categories, SubCategory, Products, Basket, Orders
from django.contrib.auth.decorators import login_required
from .forms import CreateOrderForm, CreateOrderForm2
from user.models import Users
import pprint
import random
from datetime import datetime


def generate_order_number():
    now = datetime.now()
    time_part = now.strftime("%y%m%d%H%M%S")
    random_part = str(random.randint(100, 999))  # 3 случайные цифры
    return time_part + random_part


#create orders

def buy_all_page(request):
    error_message = ""
    if request.method == "POST":
        form_data = request.POST.copy()
        unique_number = generate_order_number()
        if request.POST.get("shipping_to_user") is None:
            form_data_list = [x for x in form_data.items()]
            for y in form_data_list[2:8]:
                if y[1] == "":
                    error_message = (
                        "Произошла ошибка. При не проставлении галочки 'Заказ на данные владельца аккаунта', "
                        "поля: 'Имя', 'Область', 'Район', 'Город', 'Улица', 'Номер дома' являются обязательными к заполнению.")
                    break
            else:
                baskets = Basket.objects.filter(user=request.user)
                for x in baskets:
                    product_object = Products.objects.get(id=x.product.id)
                    form_data["product"] = product_object
                    form_data["quantity"] = x.quantity
                    form_data["order_number"] = unique_number
                    form_data["user"] = request.user
                    form_data["amount_money"] = x.product.price * x.quantity
                    form = CreateOrderForm2(data=form_data)
                    if form.is_valid():
                        form.save()
                    else:
                        print(form.errors)

                for y in baskets:
                    y.delete()

                orders = Orders.objects.filter(order_number=unique_number)

                context = {
                    "orders": orders,
                    'general_price': sum([x.product.price * x.quantity for x in orders])
                }

                return render(request, template_name="shop/order_successfully.html", context=context)
        else:
            baskets = Basket.objects.filter(user=request.user)
            for x in baskets:
                product_object = Products.objects.get(id=x.product.id)
                form_data["product"] = product_object
                form_data["quantity"] = x.quantity
                form_data["order_number"] = unique_number
                form_data["user"] = request.user
                form_data["amount_money"] = x.product.price * x.quantity
                form = CreateOrderForm2(data=form_data)
                if form.is_valid():
                    form.save()

            for y in baskets:
                y.delete()

            orders = Orders.objects.filter(user=request.user, order_number=unique_number)

            context = {
                "orders": orders,
                'general_price': sum([x.product.price * x.quantity for x in orders])
            }
            return render(request, template_name="shop/order_successfully.html", context=context)

    baskets = Basket.objects.filter(user=request.user)
    context = {
        "baskets": baskets,
        "form": CreateOrderForm(),
        "total_sum": sum(basket.sum() for basket in baskets),
        "error": error_message
    }
    return render(request, template_name="shop/buy_all_page.html", context=context)

@login_required
def buy_now_page(request, product_id):
    error_message = ""
    if request.method == "POST":
        form_data = request.POST.copy()
        unique_number = generate_order_number()
        if request.POST.get("shipping_to_user") is None:
            form_data_list = [x for x in form_data.items()]
            for y in form_data_list[3:9]:
                if y[1] == "":
                    error_message = ("Произошла ошибка. При не проставлении галочки 'Заказ на данные владельца аккаунта', "
                                     "поля: 'Имя', 'Область', 'Район', 'Город', 'Улица', 'Номер дома' являются обязательными к заполнению.")
                    break
            else:
                form_data["order_number"] = unique_number
                form = CreateOrderForm(data=form_data)
                if form.is_valid():
                    form.save()
                    basket = Basket.objects.get(product=request.POST.get("product"), user=request.user)
                    basket.delete()

                    orders = Orders.objects.filter(order_number=unique_number)

                    context = {
                        "orders": orders,
                        'general_price': sum([x.product.price * x.quantity for x in orders])
                    }
                    return render(request, template_name='shop/order_successfully.html', context=context)
        else:
            form_data["order_number"] = unique_number
            form = CreateOrderForm(data=form_data)
            if form.is_valid():
                form.save()
                basket = Basket.objects.get(product=request.POST.get("product"), user=request.user)
                basket.delete()

            orders = Orders.objects.filter(order_number=unique_number)

            context = {
                "orders": orders,
                'general_price': sum([x.product.price * x.quantity for x in orders])
            }
            return render(request, template_name='shop/order_successfully.html', context=context)

    product = get_object_or_404(Products, id=int(product_id))
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    context = {
        "baskets": Basket.objects.filter(user=request.user, product=product),
        "total_sum": sum(basket.sum() for basket in baskets),
        "form": CreateOrderForm(),
        "error": error_message
    }
    return render(request, template_name="shop/buy_now_page.html", context=context)


#basket


@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_product_plus(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_product_minus(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {
        "baskets": baskets,
        "total_sum": sum(basket.sum() for basket in baskets),
    }
    return render(request, template_name="shop/basket.html", context=context)


#all products


def products(request):
    products = Products.objects.all()
    context = {
        "title": "Каталог",
        "products": products,
        "user": request.user,
    }
    return render(request, template_name="shop/main.html", context=context)

# detail


def detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    context = {
        'product': product
    }
    return render(request, template_name="shop/detail.html", context=context)


#Categories


def all_guitars_catalog(request):
    category = Categories.objects.get(id=1)
    products = Products.objects.filter(category=category)
    context = {
        'title': 'Гитары',
        'products': products
    }
    return render(request, 'shop/main.html', context)


def all_keyboards_catalog(request):
    category = Categories.objects.get(id=2)
    products = Products.objects.filter(category=category)
    context = {
        'title': 'Клавишные',
        'products': products
    }
    return render(request, 'shop/main.html', context)


def all_drums_catalog(request):
    category = Categories.objects.get(id=3)
    products = Products.objects.filter(category=category)
    context = {
        'title': 'Ударные',
        'products': products
    }
    return render(request, 'shop/main.html', context)


def all_studio_equipments_catalog(request):
    category = Categories.objects.get(id=4)
    products = Products.objects.filter(category=category)
    context = {
        'title': 'Студийное оборудование',
        'products': products
    }
    return render(request, 'shop/main.html', context)


def all_patch_cables_catalog(request):
    category = Categories.objects.get(id=5)
    products = Products.objects.filter(category=category)
    context = {
        'title': 'Коммутация',
        'products': products
    }
    return render(request, 'shop/main.html', context)


# SubCategory


def electric_guitars_catalog(request):
    sub_category = SubCategory.objects.get(id=1)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Электрогитары', 'products': products}
    return render(request, 'shop/main.html', context)


def bass_guitars_catalog(request):
    sub_category = SubCategory.objects.get(id=2)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Бас гитары', 'products': products}
    return render(request, 'shop/main.html', context)


def acoustic_guitars_catalog(request):
    sub_category = SubCategory.objects.get(id=3)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Акустические гитары', 'products': products}
    return render(request, 'shop/main.html', context)


def classical_guitars_catalog(request):
    sub_category = SubCategory.objects.get(id=4)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Классические гитары', 'products': products}
    return render(request, 'shop/main.html', context)


def digital_pianos_catalog(request):
    sub_category = SubCategory.objects.get(id=5)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Цифровые фортепиано', 'products': products}
    return render(request, 'shop/main.html', context)


def synthesizers_catalog(request):
    sub_category = SubCategory.objects.get(id=6)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Синтезаторы', 'products': products}
    return render(request, 'shop/main.html', context)


def midi_controllers_catalog(request):
    sub_category = SubCategory.objects.get(id=7)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Миди контроллеры', 'products': products}
    return render(request, 'shop/main.html', context)


def drum_kits_catalog(request):
    sub_category = SubCategory.objects.get(id=8)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Ударные установки', 'products': products}
    return render(request, 'shop/main.html', context)


def digital_drums_catalog(request):
    sub_category = SubCategory.objects.get(id=9)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Цифровые ударные установки', 'products': products}
    return render(request, 'shop/main.html', context)


def percussions_catalog(request):
    sub_category = SubCategory.objects.get(id=10)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Перкуссии', 'products': products}
    return render(request, 'shop/main.html', context)


def drum_accessories_catalog(request):
    sub_category = SubCategory.objects.get(id=11)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Комплектующие к ударным', 'products': products}
    return render(request, 'shop/main.html', context)


def audio_interfaces_catalog(request):
    sub_category = SubCategory.objects.get(id=12)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Звуковые карты', 'products': products}
    return render(request, 'shop/main.html', context)


def studio_monitors_catalog(request):
    sub_category = SubCategory.objects.get(id=13)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Студийные мониторы', 'products': products}
    return render(request, 'shop/main.html', context)


def microphones_catalog(request):
    sub_category = SubCategory.objects.get(id=14)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Микрофоны', 'products': products}
    return render(request, 'shop/main.html', context)


def studio_headphones_catalog(request):
    sub_category = SubCategory.objects.get(id=15)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Студийные наушники', 'products': products}
    return render(request, 'shop/main.html', context)


def dj_controllers_catalog(request):
    sub_category = SubCategory.objects.get(id=16)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Dj-контроллеры', 'products': products}
    return render(request, 'shop/main.html', context)


def guitar_cables_catalog(request):
    sub_category = SubCategory.objects.get(id=17)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Кабеля гитарные', 'products': products}
    return render(request, 'shop/main.html', context)


def microphone_cables_catalog(request):
    sub_category = SubCategory.objects.get(id=18)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Кабеля микрофонные', 'products': products}
    return render(request, 'shop/main.html', context)


def speaker_cables_catalog(request):
    sub_category = SubCategory.objects.get(id=19)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Кабеля для акустических систем', 'products': products}
    return render(request, 'shop/main.html', context)


def midi_cables_catalog(request):
    sub_category = SubCategory.objects.get(id=20)
    products = Products.objects.filter(sub_category=sub_category)
    context = {'title': 'Midi-кабеля', 'products': products}
    return render(request, 'shop/main.html', context)