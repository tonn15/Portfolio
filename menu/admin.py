from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ("nom", "ingredients", "prix", "vegetarienne")
    search_fields = ["nom"]


admin.site.register(Pizza, PizzaAdmin)