from django.urls import  path
from app_menu.views import MenuApiView, MenuItemApiView, CommentView

urlpatterns = [
    path('user/menu/', MenuApiView.as_view(), name='menu'),
    path('menu/', MenuItemApiView.as_view(), name='menu' ),
    path('comment/', CommentView.as_view(), name='commend'),

]