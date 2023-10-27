from django.db import models


class Slider(models.Model):
    """ Модель Слайдера
    """
    type = models.CharField(
        max_length=30,
        verbose_name="Тип Слайдера",
    )
    title = models.CharField(
        max_length=60,
        verbose_name="Название Слайдера",
    )
    image = models.ImageField(
        upload_to="sliders/",
        verbose_name="Изображение Слайдера",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class SettingsWebsite(models.Model):
    """ Модель Настроек Вебсайта
    """
    title = models.CharField(
        max_length=30,
        verbose_name="Название",
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Номер телефона",
    )
    sliders = models.ManyToManyField(
        Slider,
        verbose_name="Слайдеры",
        blank=True,  # Не обязательно для заполнения
    )

    facebook_url = models.CharField(
        max_length=100,
        verbose_name="Ссылка на Фейсбук",
        blank=True,
        null=True,
    )
    instagram_url = models.CharField(
        max_length=100,
        verbose_name="Ссылка на Инстраграм",
        blank=True,
        null=True,
    )
    twitter_url = models.CharField(
        max_length=100,
        verbose_name="Ссылка на Твиттер",
        blank=True,
        null=True,
    )
    pinterest_url = models.CharField(
        max_length=100,
        verbose_name="Ссылка на Пинтерест",
        blank=True,
        null=True,
    )
    developer = models.CharField(
        max_length=50,
        verbose_name="Разработчик",
    )

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name = "Настройка Сайта"
        verbose_name_plural = "Настройки Сайта"
