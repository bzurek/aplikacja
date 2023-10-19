from django.contrib import admin

# Register your models here.
from .models import Person
from .models import Stanowisko
from .models import Osoba

admin.site.register(Person)
admin.site.register(Stanowisko)
admin.site.register(Osoba)