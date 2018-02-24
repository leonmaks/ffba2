from django.contrib import admin

from . import models as m


class CashRegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "org_unit", "show_order",)
    search_fields = ["name", "org_unit",]
    exclude = ("create_user", "create_dt", "modify_user", "modify_dt",)


admin.site.register(m.CashRegister, CashRegisterAdmin)
