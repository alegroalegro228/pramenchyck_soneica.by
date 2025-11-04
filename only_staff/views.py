from django.shortcuts import render
from functools import wraps
from django.contrib.auth.decorators import login_required
from shop.models import Orders
from shop.forms import ChangeOrderStatusForm


def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, template_name="only_staff/404.html")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def unique_order(status):
    orders = Orders.objects.filter(status=status).order_by("-created_timestamp")
    unique_values = {order.order_number: order for order in orders}
    return list(x for x in unique_values.values())


def search_order(order_number):
    orders = Orders.objects.filter(order_number=order_number)
    print(orders)
    unique_values = {order.order_number: order for order in orders}
    print(unique_values)
    print(list(x for x in unique_values.values()))
    return list(x for x in unique_values.values())


@login_required
@superuser_required
def only_staff_new(request):
    if request.method == "POST":
        order_number = request.POST.get("order_number")
        searched = search_order(order_number)
        context = {
            "title": "Найденные",
            "orders": searched
        }
        return render(request, template_name='only_staff/only_staff_main.html', context=context)
    else:
        context = {
            "title": "Новые",
            "orders": unique_order("created"),
        }
        return render(request, template_name='only_staff/only_staff_main.html', context=context)


@login_required
@superuser_required
def only_staff_in_work(request):
    context = {
        "title": "В работе",
        "orders": unique_order("in_work"),
    }
    return render(request, template_name='only_staff/only_staff_main.html', context=context)


@login_required
@superuser_required
def only_staff_completed(request):
    context = {
        "title": "Завершенные",
        "orders": unique_order("completed"),
    }
    return render(request, template_name='only_staff/only_staff_main.html', context=context)


@login_required
@superuser_required
def only_staff_canceled(request):
    context = {
        "title": "Отмененные",
        "orders": unique_order("canceled"),
    }
    return render(request, template_name='only_staff/only_staff_main.html', context=context)


def order_detail(request, order_number):
    if request.method == "POST":
        order_number = request.POST.get("order_number")
        order_new_status = request.POST.get("status")
        orders = Orders.objects.filter(order_number=order_number)
        print(request.POST)
        for order in orders:
            order.status = order_new_status
            order.save()
    orders = Orders.objects.filter(order_number=order_number)
    context = {
        "orders": orders,
        "form": ChangeOrderStatusForm(initial={"status": orders[0].status}),
        "total_sum": sum([x.amount_money for x in orders])
    }
    return render(request, template_name="only_staff/administration_detail.html", context=context)


