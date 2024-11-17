

from rest_framework import serializers

from app_menu.models import MenuItemModel, CommentModel


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemModel
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('imaeg', None)
        menu_item = MenuItemModel.objects.create(**validated_data)
        if image:
            menu_item.image = image
            menu_item.save()
        return menu_item

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'image' and value:
                instance.image = value
            setattr(instance, key, value)
        instance.save()
        return instance



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

    def create(self, validated_data):
        comment = CommentModel(**validated_data)
        comment.save()
        return comment
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance