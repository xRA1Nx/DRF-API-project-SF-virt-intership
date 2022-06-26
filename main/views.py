from rest_framework.generics import get_object_or_404

from main.serializers import *
from main.models import Coards, PerevalAdd, PerevalImages, User, PerevalUser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


class PerevalView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == "list":
            return PerevalAdd.objects.all()
        elif self.action in ["create", "update"]:
            return PerevalAdd.objects.get(pk=self.kwargs['pk'])

    def get_serializer_class(self):
        if self.action == "list":
            return PerevalsSerializer
        elif self.action in ["retrieve", "create"]:
            return PerevalSerializer
        elif self.action == "update":
            return PerevalUpdSerializer

    # переписываем метод. В случае если нет такой страницы возвращаем 404 ответ
    def retrieve(self, request, *args, **kwargs, ):
        queryset = PerevalAdd.objects.filter(id=self.kwargs["pk"])
        item = get_object_or_404(queryset)
        serializer = PerevalSerializer(item)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        queryset = PerevalAdd.objects.filter(id=self.kwargs["pk"])
        item = get_object_or_404(queryset)
        serializer = PerevalUpdSerializer(item)
        return Response(serializer.data)




class PhotoListView(APIView):
    """Список фотографий"""

    def get(self, request):
        photos = PerevalImages.objects.all()
        serializer = PerevalsSerializer(photos, many=True)
        return Response(serializer.data, status=200)


class PhotoDeteilView(APIView):
    """Детализация перевала"""

    def get(self, request, pk):
        try:
            photo = PerevalImages.objects.get(id=pk)
        except:
            return Response({"error": f"id={pk} doesn`t exists "}, status=400)

        serializer = PhotoDeteilSerializer(photo)
        return Response(serializer.data, status=200)


class PhotoAddView(viewsets.ModelViewSet):
    """добавляем фотографию"""
    queryset = PerevalImages.objects.all()
    serializer_class = PhotoAddSerializer

    def create(self, request):
        photo = PhotoAddSerializer(data=request.data)
        if photo.is_valid():
            photo.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response({"error": "validation error"}, status=400)


class UsersListView(APIView):
    """список пользователей"""

    def get(self, request):
        item = User.objects.all()
        serializer = UsersSerializer(item, many=True)
        return Response(serializer.data, status=200)


class UserDeteilView(APIView):
    """детальная информация по пользователю"""

    def get(self, request, pk):
        try:
            item = User.objects.get(id=pk)
        except:
            return Response({"error": f"id={pk} doesn`t exists "}, status=400)
        serializer = UserDeteilSerializer(item)
        return Response(serializer.data, status=200)


class UserAddView(viewsets.ModelViewSet):
    """Создание пользователя"""
    queryset = User.objects.all()
    serializer_class = UserAddSerializer

    def create(self, request):
        item = UserAddSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response({"error": "validation error"}, status=400)


class PerevalUserAddView(APIView):
    def post(self, request):
        item = PerevalUserSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response({"error": "validation error"}, status=400)


class PerevalUsersListView(APIView):
    """список пользователей"""

    def get(self, request):
        item = PerevalUser.objects.all()
        serializer = PerevalUserSerializer(item, many=True)
        return Response(serializer.data, status=200)
