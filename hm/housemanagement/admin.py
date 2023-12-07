from django.contrib import admin
from .models import Person
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'phone_number1', 'phone_number2',
                    'email', 'birth_date')
    ordering = ['-time_create']
    list_editable = ('last_name', 'patronymic', 'phone_number1', 'phone_number2',
                     'email', 'birth_date',)
    list_per_page = 5
    search_fields = ['first_name', 'last_name', 'patronymic', 'phone_number1', 'phone_number2',
                     'email', 'birth_date']
