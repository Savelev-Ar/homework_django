from django.db import models


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
