from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Наименование',
        help_text='Введите название категории'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Наименование',
        help_text='Введите название'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание',
        blank=True,
        null=True
    )
    preview = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Цена',
        help_text='Введите цену'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата создания записи'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения',
        help_text='Дата последнего изменения записи'
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        verbose_name="Создан пользователем",
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    number_version = models.IntegerField(
        verbose_name='Версия',
        help_text='Введите номер версии продукта'
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Название версии',
        help_text='Введите название версии продукта'
    )

    is_current_version = models.BooleanField(
        verbose_name='Признак версии',
        help_text='Признак текущей версии',
        default=False
    )

    def __str__(self):
        return f'{self.name} {self.number_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('name',)
