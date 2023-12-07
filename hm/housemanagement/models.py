from django.db import models

# Create your models here.


class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(
        max_length=50, verbose_name='Отчество', blank=True, null=True)
    phone_number1 = models.CharField(
        max_length=15, verbose_name='Телефонный номер 1')
    phone_number2 = models.CharField(
        max_length=15, verbose_name='Телефонный номер 2', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', unique=False)
    birth_date = models.DateField(
        verbose_name='Дата рождения', blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name='Пол', blank=True, null=True)
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} {self.phone_number1} {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]