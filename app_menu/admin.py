from django.contrib import admin

from app_menu.models import UserModel, MenuItemModel, CommentModel


admin.site.register(MenuItemModel)
admin.site.register(CommentModel)


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'address')

