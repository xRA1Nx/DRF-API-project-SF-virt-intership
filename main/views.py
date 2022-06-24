from main.serializers import CoardsSerializer, PerevalsSerializer, \
    PerevalSerializer, PhotoAddSerializer
from main.models import Coards, PerevalAdd, PerevalImages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


class PerevalListView(APIView):
    """вывод списка всех координат"""

    def get(self, request):
        perevals = PerevalAdd.objects.all()
        serializer = PerevalsSerializer(perevals, many=True)
        return Response(serializer.data, status=200)


class PerevalCreateView(APIView):
    """вывод списка всех координат"""

    def post(self, request):
        pereval = PerevalsSerializer(data=request.data)
        if pereval.is_valid():
            pereval.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response({"error": "validation error"}, status=400)


class PerevalDeteilView(APIView):
    """Детализация перевала"""

    def get(self, request, pk):
        try:
            pereval = PerevalAdd.objects.get(id=pk)
        except:
            return Response({"error": f"id={pk} doesn`t exists "}, status=400)

        serializer = PerevalSerializer(pereval)
        return Response(serializer.data, status=200)


class PhotoListView(APIView):
    """Список фотографий"""

    def get(self, request):
        photos = PerevalImages.objects.all()
        serializer = PerevalsSerializer(photos, many=True)
        return Response(serializer.data, status=200)


class PhotoAddView(APIView):
    """добавляем фотографию"""

    def post(self, request):
        photo = PhotoAddSerializer(data=request.data)
        if photo.is_valid():
            photo.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response({"error": "validation error"}, status=400)
