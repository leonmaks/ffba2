from django.contrib import admin
# from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import OrgUnit, Profile


class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False


class UserAdmin(UserAdmin):
	inlines = (ProfileInline, )


class OrgUnitAdmin(admin.ModelAdmin):
# class OrgUnitAdmin(SimpleHistoryAdmin):
	list_display = ("name", "up",)
	search_fields = ["name", "up",]
	exclude = ("create_user", "create_dt", "modify_user", "modify_dt",)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(OrgUnit, OrgUnitAdmin)
