from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from main.serializers import *
from main.models import  PerevalAdd, PerevalImages, User, PerevalUser, PerevalAreas

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins


class PerevalUserView(viewsets.ModelViewSet):
    queryset = PerevalUser.objects.all()
    serializer_class = PerevalUserSerializer


class AreasView(viewsets.ModelViewSet):
    queryset = PerevalAreas.objects.all()
    serializer_class = AreasSerializer


class PerevalView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = PerevalAdd.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PerevalsSerializer
        elif self.action == "update":
            return PerevalUpdSerializer
        else:
            return PerevalSerializer

    # переписываем метод. В случае если нет такой страницы возвращаем 404 ответ
    # def retrieve(self, request, *args, **kwargs, ):
    #     queryset = PerevalAdd.objects.filter(id=kwargs["pk"])
    #     item = get_object_or_404(queryset)
    #     serializer = PerevalSerializer(item)
    #     return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        try:
            instance = PerevalAdd.objects.get(pk=pk)
        except:
            return Response({"error:object doesn`t exists"}, status=400)

        if instance.status != "new":
            return Response({"message": "u can change objects only with status new", "state": 0}, status=400)
        else:
            # для метода upd обязательно нужно передать instance, иначе сериализатор будет воспринимать это как create
            serializer = PerevalUpdSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)


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
        serializer = PerevalUserSerializer(data=item, many=True)
        return Response(serializer.data, status=200)
