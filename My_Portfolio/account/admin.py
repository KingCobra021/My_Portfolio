from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

#admin.site.register(Account)
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ("username","email","last_login","is_admin","is_staff")# what info about the user is getting dispalyed
    search_fields = ("username", "email")# search fields
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
