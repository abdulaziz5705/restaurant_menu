from django.contrib import admin

from app_menu.models import UserModel, MenuItemModel, CommentModel, CategoryModel


admin.site.register(UserModel)
admin.site.register(CategoryModel)
admin.site.register(MenuItemModel)
admin.site.register(CommentModel)

