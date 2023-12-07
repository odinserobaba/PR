from django.contrib import admin
from .models import Person, City, Address
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


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name']
    list_per_page = 5
    search_fields = ['name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'street',
                    'house_number',)
    ordering = ['house_number']
    list_per_page = 5
    search_fields = ['house_number', 'floor', 'address',
                     'building_number', 'entrance_number', 'owner']

    def city_name(self, obj):
        return obj.city.name
    city_name.short_description = 'Город'
