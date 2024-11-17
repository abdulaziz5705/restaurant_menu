from django.shortcuts import render
from django.template.defaulttags import comment
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from app_menu.models import MenuItemModel, CommentModel
from app_menu.serializer import MenuItemSerializer, CommentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class MenuItemApiView(APIView):
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        menu = MenuItemModel.objects.all()
        serializer = MenuItemSerializer(menu, many=True).data
        return Response(serializer, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer_data = MenuItemSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()
        response = {"success": True, "message": "Menu item created", "data": serializer_data.data}
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer_data = MenuItemSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()
        response = {"success": True, "message": "Menu item updated", "data": serializer_data.data}
        return Response(response, status=status.HTTP_201_CREATED)

    def patch(self, request):
        serializer_data = MenuItemSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()
        response = {"success": True, "message": "Menu item updated", "data": serializer_data.data}
        return Response(response, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None):
        menu = MenuItemModel.objects.get_object_or_404(pk=pk)
        menu.delete()
        response = {"success": True, "message": "Menu item deleted"}
        return Response(response, status=status.HTTP_201_CREATED)
class MenuApiView(APIView):
    queryset = MenuItemModel.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [AllowAny]
    def get(self, request):
        menu = MenuItemModel.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentView(APIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        comment = CommentModel.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {"success": True, "message": "Comment created", "data": serializer.data}
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {"success": True, "message": "Comment updated", "data": serializer.data}
        return Response(response, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None):
        comment = CommentModel.objects.all()
        serializer = CommentSerializer(data=request.data)
        comment.delete()
        response = {"success": True, "message": "Comment deleted", "data": serializer.data}
        return Response(response, status=status.HTTP_201_CREATED)











