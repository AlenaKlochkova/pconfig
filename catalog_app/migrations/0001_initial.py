# Generated by Django 4.0.4 on 2022-06-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Корпус',
                'verbose_name_plural': 'Корпуса',
            },
        ),
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Кулер',
                'verbose_name_plural': 'Кулеры',
            },
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Жесткий диск',
                'verbose_name_plural': 'Жесткие диски',
            },
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Материнская плата',
                'verbose_name_plural': 'Материнские платы',
            },
        ),
        migrations.CreateModel(
            name='Powerunit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Блок питания',
                'verbose_name_plural': 'Блоки питания',
            },
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Процессор',
                'verbose_name_plural': 'Процессоры',
            },
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Оперативная память',
            },
        ),
        migrations.CreateModel(
            name='Videocard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Видеокарта',
                'verbose_name_plural': 'Видеокарты',
            },
        ),
    ]
