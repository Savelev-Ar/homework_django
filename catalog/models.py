from django.db import models


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

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Blog(models.Model):
    header = models.CharField(
        max_length=150,
        verbose_name='Заголовок',
        help_text='Введите заголовок публикации'
    )
    slug = models.CharField(
        verbose_name='челоурль',
        help_text='человекопонятный URL',
        blank=True,
        null=True
    )
    content = models.TextField(
        verbose_name='Содержимое',
        help_text='Введите содержимое',
        blank=True,
        null=True
    )
    preview = models.ImageField(
        upload_to='blog/',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата создания записи'
    )
    is_posted = models.BooleanField(
        verbose_name='Опубликовано',
        help_text='Признак публикации',
        default=False
    )
    view_count = models.PositiveBigIntegerField(
        verbose_name='Просмотры',
        help_text='Количество просмотров',
        default=0
    )

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
