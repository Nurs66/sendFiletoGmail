from django.db import models

SERVICES = (
    ('Онлайн консультация юриста', 'Онлайн консультация юриста'),
    ('Онлайн консультация бухгалтера', 'Онлайн консультация бухгалтера'),
)


class Person(models.Model):
    fio = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        db_index=True,
        blank=True, null=True,
    )
    service = models.CharField(
        max_length=255,
        verbose_name='Услуга',
        choices=SERVICES,
        blank=True, null=True,
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Телефон',
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
        return self.fio

    class Meta:
        ordering = ('-id',)
