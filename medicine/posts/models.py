from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

UPLOAD_DIR = "posts/"


class Post(models.Model):
    text = models.TextField(verbose_name="Текст отзыва", help_text="Введите текст отзыва")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.CharField(max_length=200, verbose_name="Автор")

    image = models.ImageField("Картинка", upload_to=UPLOAD_DIR, blank=True)
    visible = models.BooleanField(default=False, verbose_name="Показывать")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.text[:15]


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    for_main_page = models.BooleanField(
        verbose_name="Показывать на главной странице", default=False
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ("pk",)

    def __str__(self):
        return f"{self.name} {self.price} р"
