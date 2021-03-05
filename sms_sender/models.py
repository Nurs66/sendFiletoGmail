from django.core.validators import RegexValidator
from django.db import models

phone_number_regex = RegexValidator(
    regex=r'^(\+996)\d{9}$',
    message=(
        "Телефон должен быть в формате +996[код][номер]"
    )
)


class Person(models.Model):
    first_name = models.CharField(
        max_length=255,
        db_index=True,
        blank=True, null=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        db_index=True,
        blank=True, null=True,
        verbose_name='Фамилия'
    )
    middle_name = models.CharField(
        max_length=255,
        db_index=True,
        blank=True, null=True,
        verbose_name='Отчество'
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Телефон',
        validators=[phone_number_regex],
        null=True, blank=True
    )
    email = models.EmailField(
        blank=True, null=True,
        verbose_name='Почта'
    )
    content = models.TextField(
        blank=True, null=True,
        verbose_name='Сообщение (комментарий)'
    )
    file = models.ImageField(
        upload_to='files',
        null=True, blank=True,
        verbose_name='Файл'
    )

    def __str__(self):
        return f"{self.first_name} -- {self.last_name}"

    class Meta:
        ordering = ('-id',)
