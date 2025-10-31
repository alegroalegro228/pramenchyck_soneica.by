from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    telephone = models.CharField(verbose_name="Номер телефона", max_length=14, default="+375 00 000-00-00")
    region = models.CharField(verbose_name="Область", max_length=20, null=True, blank=True)
    district = models.CharField(verbose_name="Район", max_length=150, null=True, blank=True)
    city = models.CharField(verbose_name="Город", max_length=150, null=True, blank=True)
    street = models.CharField(verbose_name="Улица", max_length=150, null=True, blank=True)
    house_number = models.IntegerField(verbose_name="Номер дома", null=True, blank=True)
    entrance_number = models.IntegerField(verbose_name="Номер подъезда", null=True, blank=True)
    flat_number = models.IntegerField(verbose_name="Номер квартиры", null=True, blank=True)
    post_index = models.CharField(verbose_name="Почтовый индекс", max_length=10, null=True, blank=True)

