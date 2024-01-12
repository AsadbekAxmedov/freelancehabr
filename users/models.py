from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
CUSTOMER = 'customer'
FREELANCER = 'freelancer'

TYPES = (
   (CUSTOMER, 'Заказчик'),
   (FREELANCER, 'Фрилансер')
)

class User(AbstractUser):
    role = models.CharField(max_length=200, choices=TYPES)
    avatar = models.ImageField(null=True, blank=True)
    is_activated = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        db_table = 'users_user'
        app_label = 'users'