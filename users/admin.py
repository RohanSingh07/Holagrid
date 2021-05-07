from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# this is required bcz when we add users in admin it says to first give username and password
UserAdmin.add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','username', 'password1', 'password2')}
        ),
    )


class AccountAdmin(UserAdmin):
    list_display = (
        'phone','username','date_joined','last_login','is_admin','is_staff'
    )
    search_fields = ('phone','username') # we can search for these
    readonly_fields = ('date_joined','last_login') # these cannot be changed from admin page

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () # required , but i am not sure what is does

admin.site.register(Account,AccountAdmin)
