from main.serializers import CoardsSerializer, PerevalAddSerializer
from main.models import Coards, PerevalAdd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


class CoardsListView(APIView):
    """вывод списка всех координат"""

    def get(self, request):
        coards = Coards.objects.all()
        serializer = CoardsSerializer(coards, many=True)
        return Response(serializer.data)

    def post(self, request):
        coards = CoardsSerializer(data=request.data)
        if coards.is_valid():
            coards.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response(status=400)


class PerevalListView(APIView):
    """вывод списка всех координат"""

    def get(self, request):
        perevals = PerevalAdd.objects.all()
        serializer = PerevalAddSerializer(perevals, many=True)
        return Response(serializer.data)

    def post(self, request):
        pereval = PerevalAddSerializer(data=request.data)
        if pereval.is_valid():
            pereval.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response(status=400)
