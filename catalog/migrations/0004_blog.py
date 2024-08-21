# Generated by Django 4.2.14 on 2024-08-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(help_text='Введите заголовок публикации', max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, help_text='человекопонятный URL', null=True, verbose_name='челоурль')),
                ('content', models.TextField(blank=True, help_text='Введите содержимое', null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='blog/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания записи', verbose_name='Дата создания')),
                ('is_posted', models.BooleanField(default=False, help_text='Признак публикации', verbose_name='Опубликовано')),
                ('view_count', models.PositiveBigIntegerField(default=0, help_text='Количество просмотров', verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'публикации',
            },
        ),
    ]
