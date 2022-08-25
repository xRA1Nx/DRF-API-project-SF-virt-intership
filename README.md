Виртуальная стажировка от SkillFactory (мой первый проект на DRF)

Разработана API для спортивно-туристического мобильного приложения с помощью Django Rest Framework.

http://127.0.0.1:8000/api/v1/submit-data/pereval/ - список всех перевалов, добавление нового перевала
http://127.0.0.1:8000/api/v1/submit-data/pereval/<id> - детальная информация о перевале с указанным id. Изменение данных перевала со статусом new(не прошедших модерацию)

http://127.0.0.1:8000/api/v1/submit-data/pereval-user/ - список вспомогательной таблицы m2m связи с отношением перевала к пользователю, добавление новой записи перевал-пользователь
http://127.0.0.1:8000/api/v1/submit-data/pereval-user/<id> - детальная информация о связи перевал-пользователь с указанным id. Изменение данных перевала-пользователя


http://127.0.0.1:8000/api/v1/submit-data/areas/ - список всех вершин, добавление новой вершины
http://127.0.0.1:8000/api/v1/submit-data/areas/<id>  - детальная информация о вершине с указанным id. Изменение данных перевала.

http://127.0.0.1:8000/api/v1/submit-data/users/ - список всех пользователей
http://127.0.0.1:8000/api/v1/submit-data/users/<id> - детальная информация о пользователе с указанным id
http://127.0.0.1:8000/api/v1/submit-data/users/add/ - добавление нового пользователя

http://127.0.0.1:8000/api/v1/submit-data/photos/ - список всех фотографий
http://127.0.0.1:8000/api/v1/submit-data/photos/<id> - детальная информация о фотографии с указанным id
http://127.0.0.1:8000/api/v1/submit-data/photos/add/ - добавление новой фотографии

Приложение main покрыто тестами в т.ч. проведена ручная отладка

основная View отвечающая за отображение данных модели PerevalAdd оформлена на viewset.ModelView с применением роутера
для данного представления переопределены методы get_serialaer и list и update т.к. от ТЗ состояло из нетиповых задач

Пример метода update:

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        try:
            instance = PerevalAdd.objects.get(pk=pk)
        except:
            return Response({"error:object doesn`t exists"}, status=400)
        #в случае если status != new, возвращаем ошибку и 400 статус
        if instance.status != "new":
            return Response({"message": "u can change objects only with status new", "state": 0}, status=400)
        else:
            # для метода upd обязательно нужно передать instance, иначе сериализатор будет воспринимать это как create
            serializer = PerevalUpdSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"state": 1}, status=200)




Также в проекте использовались представления сделанные на основании APIView, для обучающей цели. Как таковой необходимости в APIView в проекте нет, и viewSet позволил с применением раутера был бы более оптимальным решением.


