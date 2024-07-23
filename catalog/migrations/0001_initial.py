# Generated by Django 4.2.14 on 2024-07-23 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название категории', max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, help_text='Введите описание', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, help_text='Введите описание', null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='products/', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену', max_digits=9, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания записи', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата последнего изменения записи', verbose_name='Дата изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
    ]
