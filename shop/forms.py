from django import forms
from .models import Orders, Comments


class CreateOrderForm(forms.ModelForm):
    Payment_method_choices = [
        ("courier", "Курьером"),
        ("bel-post", "Бел-почта"),
        ("Euro-post", "Евро-почта")
    ]

    Shipping_method_choices = [
        ("Erip", "Ерип"),
        ("Cash-to-the-courier", "Наличными курьеру"),
        ("bank-card", "Банковская карта")
    ]

    shipping_to_user = forms.BooleanField(widget=forms.CheckboxInput(attrs={
    }), required=False)

    name_client = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Имя"
    }), required=False)

    region = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Область"
    }), required=False)
    district = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Район"
    }), required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Город"
    }), required=False)
    street = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Улица"
    }), required=False)
    house_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Номер дома"
    }), required=False)
    entrance_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Подъезд"
    }), required=False)
    flat_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Квартира"
    }), required=False)
    post_index = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Почтовый индекс"
    }), required=False)

    telephone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "value": "+375 00 000-00-00"
    }), required=False)

    payment_method = forms.ChoiceField(choices=Payment_method_choices, widget=forms.Select(attrs={
        "class": "form-control",
    }))

    shipping_method = forms.ChoiceField(choices=Shipping_method_choices, widget=forms.Select(attrs={
        "class": "form-control",
    }))

    comment = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Коментарий к заказу"
    }), required=False)

    class Meta:
        model = Orders
        fields = ("order_number", "product", "quantity", "user", "shipping_to_user", "name_client", "region", "district", "city", "street", "house_number",
                  "entrance_number", "flat_number", "post_index", "telephone", "payment_method",
                  "shipping_method", "comment", "amount_money")


class CreateOrderForm2(forms.ModelForm):
    shipping_to_user = forms.BooleanField(widget=forms.CheckboxInput(attrs={
    }), required=False)

    name_client = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Имя"
    }), required=False)

    region = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Область"
    }), required=False)
    district = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Район"
    }), required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Город"
    }), required=False)
    street = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Улица"
    }), required=False)
    house_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Номер дома"
    }), required=False)
    entrance_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Подъезд"
    }), required=False)
    flat_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Квартира"
    }), required=False)
    post_index = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Почтовый индекс"
    }), required=False)

    telephone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "value": "+375 00 000-00-00"
    }), required=False)

    payment_method = forms.ChoiceField(choices=CreateOrderForm.Payment_method_choices, widget=forms.Select(attrs={
        "class": "form-control",
    }))

    shipping_method = forms.ChoiceField(choices=CreateOrderForm.Shipping_method_choices, widget=forms.Select(attrs={
        "class": "form-control",
    }))

    comment = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Коментарий к заказу"
    }), required=False)

    class Meta:
        model = Orders
        fields = ("order_number", "product", "quantity", "user", "shipping_to_user", "name_client", "region", "district", "city", "street",
                  "house_number",
                  "entrance_number", "flat_number", "post_index", "telephone", "payment_method",
                  "shipping_method", "comment", "amount_money")


class CommentForm(forms.ModelForm):

    text = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Ваш комментарий"
    }))

    class Meta:
        model = Comments
        fields = ("product", "user", "text")


class ChangeOrderStatusForm(forms.ModelForm):
    statuses = [
        ("created", "Создан"),
        ("in_work", "В работе"),
        ("completed", "Завершен"),
        ("canceled", "Отменен"),
    ]

    status = forms.ChoiceField(choices=statuses, widget=forms.Select(attrs={
        "class": "form-control",
    }))

    class Meta:
        model = Orders
        fields = ("status",)


