from django.db import models
from user.models import Users
import uuid
from shortuuidfield import ShortUUIDField


class Categories(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.sub_category_name



    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Products(models.Model):
    image = models.ImageField(name="image", upload_to="media/products_images", default=0)
    name = models.CharField(name="name", max_length=400)
    weight = models.FloatField(name="weight", default=0)
    length = models.FloatField(name="length", default=0)
    width = models.FloatField(name="width", default=0)
    country = models.CharField(name="country", max_length=50)
    description = models.TextField(name="description", null=True, blank=True)
    price = models.FloatField(name="price", default=0)
    quantity = models.PositiveIntegerField(name="quantity", default=0)
    category = models.ForeignKey(name="category", to=Categories, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(name="sub_category", to=SubCategory, default=300, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина для {self.user.username} / товар {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity


class Orders(models.Model):
    statuses = [
        ("canceled", "Отменен"),
        ("created", "Создан"),
        ("in_work", "В работе"),
        ("completed", "Завершен"),
    ]

    uid = ShortUUIDField(unique=True, editable=False, auto_created=True)
    order_number = models.CharField(max_length=15, default="000000000000")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    shipping_to_user = models.BooleanField(verbose_name="Доставка владельцу аккаунта", default=False)
    name_client = models.CharField(verbose_name="Имя", max_length=100, null=True, blank=True)
    region = models.CharField(verbose_name="Область", max_length=20, null=True, blank=True)
    district = models.CharField(verbose_name="Район", max_length=150, null=True, blank=True)
    city = models.CharField(verbose_name="Город", max_length=150, null=True, blank=True)
    street = models.CharField(verbose_name="Улица", max_length=150, null=True, blank=True)
    house_number = models.IntegerField(verbose_name="Номер дома", null=True, blank=True)
    entrance_number = models.IntegerField(verbose_name="Номер подъезда", null=True, blank=True)
    flat_number = models.IntegerField(verbose_name="Номер квартиры", null=True, blank=True)
    post_index = models.CharField(verbose_name="Почтовый индекс", max_length=10, null=True, blank=True)
    telephone = models.CharField(verbose_name="Номер телефона", max_length=17, default="+375 00 000-00-00", null=True, blank=True)
    payment_method = models.CharField(max_length=50)
    shipping_method = models.CharField(max_length=50)
    comment = models.TextField(verbose_name="Комментарий к заказу", null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=statuses, default="created", auto_created=True)
    amount_money = models.FloatField(verbose_name="Сумма итого", default=0)

    def __str__(self):
        return "Заказ #%s" % self.order_number






class Comments(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    text = models.TextField()
    date_timestamp = models.DateTimeField(auto_now_add=True)