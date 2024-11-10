from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)




class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'





