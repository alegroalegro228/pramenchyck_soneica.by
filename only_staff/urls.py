from django.urls import path
from .views import only_staff_new, only_staff_in_work, only_staff_canceled, only_staff_completed, order_detail


app_name = "only_staff"


urlpatterns = [
    path('', only_staff_new, name='only_staff_new'),
    path('in_work/', only_staff_in_work, name='only_staff_in_work'),
    path('completed/', only_staff_completed, name='only_staff_completed'),
    path('canceled/', only_staff_canceled, name='only_staff_canceled'),
    path('order-detail/<int:order_number>', order_detail, name='order_detail')
]