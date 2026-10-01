from django.contrib import admin
from .models import Reg_Details


class Reg_DetailsAdmin(admin.ModelAdmin):
    list_display = ("name","password","email", "address")

admin.site.register(Reg_Details, Reg_DetailsAdmin)