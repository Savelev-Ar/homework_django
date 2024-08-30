from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='адрес почты',
        help_text='введите адрес электрической почты'
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='телефон',
        help_text='Введите номер телефона',
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        upload_to='users/',
        verbose_name='Аватар',
        help_text='Загрузитэ рисунок аватара',
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=35,
        verbose_name='Страна',
        help_text='Введите название страны',
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []