from django.db import models
from users.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

PC_300 = "PC_300"
P1_200 = "P1_200"
P24_200 = "P11_200"


ADVERTISING = ((PC_300, "300 кр."), (P1_200, "200 кр."), (P24_200, "200 кр."))


HOUR = "HOUR"
PROJECT = "PROJECT"
NEGOTIABLE = "NEGOTIABLE"

PRICE = ((HOUR, "за час"), (PROJECT, "за проект"), (NEGOTIABLE, "договорная"))


class Order(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextUploadingField(null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    price_type = models.CharField(max_length=50, choices=PRICE)
    advertising = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    technology = models.ManyToManyField("Technology", related_name="order_technology")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="responses")
    offer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.order.title


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
