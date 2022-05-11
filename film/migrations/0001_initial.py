# Generated by Django 4.0.4 on 2022-05-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название награды')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/award/%Y/%m/%d', verbose_name='Фото награды')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание награды')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска награды')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг награды')),
            ],
            options={
                'verbose_name': 'Награда',
                'verbose_name_plural': 'Награды',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название жанра')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание жанра')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('date_of_birth', models.DateTimeField(verbose_name='Дата рождения')),
                ('profession', models.CharField(choices=[('1', 'STARRING'), ('2', 'DIRECTOR'), ('3', 'PRODUCER'), ('4', 'OPERATOR'), ('5', 'COMPOSER'), ('6', 'MOUNTING')], max_length=255, verbose_name='Професси')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг человека')),
                ('award', models.ManyToManyField(blank=True, to='film.award', verbose_name='Награды')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('cover', models.ImageField(blank=True, help_text='Большой постер фильма(рекомендуемый размер загрузки - "Тут должен быть размер загрузки, который мне скажут с Front")', null=True, upload_to='photo/cover/%Y/%m/%d', verbose_name='Основная обложка фильма')),
                ('covet_mini', models.ImageField(blank=True, help_text='Маленький постер фильма, который можно указать в лентепользователя или в категории - "ТОП - 10"(рекомендуемый размерзагрузки-"Тут должен быть размер загрузки, который мне скажут с Front"))', null=True, upload_to='photo/cover_mini', verbose_name='Миниатюрная обложка фильма')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание фильма')),
                ('year', models.DateTimeField(verbose_name='Год выпуска фильма')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна производства')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возростное ограничение')),
                ('time', models.FloatField(verbose_name='Время показа')),
                ('rating', models.CharField(blank=True, help_text='Рейтинг филмьа согласно какому-либо изданию(кинопоиск и тд...)', max_length=255, null=True, verbose_name='Рэйтинг')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг фильма')),
                ('awards', models.ManyToManyField(blank=True, to='film.award', verbose_name='Награды фильма')),
                ('composer', models.ManyToManyField(related_name='composer', to='film.people', verbose_name='Композитор фильма')),
                ('director', models.ManyToManyField(related_name='director', to='film.people', verbose_name='Режисер фильма')),
                ('genre', models.ManyToManyField(to='film.genre', verbose_name='Жанры фильма')),
                ('mounting', models.ManyToManyField(related_name='mounting', to='film.people', verbose_name='Монтажер фильма')),
                ('operator', models.ManyToManyField(related_name='operator', to='film.people', verbose_name='Оператор фильма')),
                ('producer', models.ManyToManyField(related_name='producer', to='film.people', verbose_name='Продюсер фильма')),
                ('starring', models.ManyToManyField(related_name='starring', to='film.people', verbose_name='Главные актеры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
