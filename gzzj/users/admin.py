from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models
from users.models import Users, Dept


class UsersModels(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'user_name', 'dept', 'is_manager', 'user_remark', 'groups')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      )}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        # 'groups', 'user_permissions'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'user_name', 'dept', 'is_manager',
                       'user_remark', 'groups')
        }),
    )

    list_display = ('id', 'username', 'user_name', 'dept', 'is_manager', 'user_remark')


admin.site.register(Users, UsersModels)
admin.site.register(Dept)

