from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PerevalAdd

from .models import *


class PerevalAddTests(APITestCase):
    def setUp(self) -> None:
        user_test1 = User.objects.create(
            email="test1@test1.ru")

        pereval_test1 = PerevalAdd.objects.create(
            title="for_test3",
            beautyTitle="test",
            other_titles="test",
            connect="test",
            level_winter="test",
            level_summer="test",
            level_autumn="test",
            level_spring="test",
            latitude=23.23,
            longitude=23.23,
            height=2323
        )

        pereval_test2 = PerevalAdd.objects.create(
            status="pending",
            title="test",
            beautyTitle="test",
            other_titles="test",
            connect="test",
            level_winter="test",
            level_summer="test",
            level_autumn="test",
            level_spring="test",
            latitude=23.23,
            longitude=23.23,
            height=2323
        )

        pereval_test1.save()
        pereval_test1.users.add(user_test1)
        pereval_test2.save()

    def test_1_create_pereval(self):
        url = 'http://127.0.0.1:8000/api/v1/submit-data/pereval/'
        data = {
            "photos": [],
            "areas": [],
            "users": [],
            "title": "unit-test",
            "beautyTitle": "fsdafsadf",
            "other_titles": "sadf",
            "connect": "safsdafsadf",
            "level_winter": "fsdafasf",
            "level_summer": "sdfasfasf",
            "level_autumn": "fsadfas",
            "level_spring": "ffsadfsaf",
            "latitude": 22.0,
            "longitude": 22.0,
            "height": 2222,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PerevalAdd.objects.count(), 3)
        self.assertEqual(PerevalAdd.objects.all()[2].title, 'unit-test')

    def test_2_update_pereval(self):
        url_1 = 'http://127.0.0.1:8000/api/v1/submit-data/pereval/4/'
        url_2 = 'http://127.0.0.1:8000/api/v1/submit-data/pereval/5/'
        data = {
            "photos": [],
            "areas": [],
            "users": [],
            "title": "unit-test-upd",
            "beautyTitle": "unit-test-updf",
            "other_titles": "unit-test-upd",
            "connect": "unit-test-upd",
            "level_winter": "unit-test-upd",
            "level_summer": "unit-test-upd",
            "level_autumn": "unit-test-upd",
            "level_spring": "unit-test-upd",
            "latitude": 22.0,
            "longitude": 22.0,
            "height": 2222,
        }
        # проверяем upd перевала со статусом new
        response = self.client.put(url_1, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PerevalAdd.objects.count(), 2)
        self.assertEqual(PerevalAdd.objects.filter(title='unit-test-upd').exists(), True)
        self.assertEqual(response.data['state'], 1)

        # проверяем upd перевала со статусом != new
        response = self.client.put(url_2, data, format="json")
        self.assertEqual(response.data['state'], 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_3_get_perevals_by_user_email(self):
        url = 'http://127.0.0.1:8000/api/v1/submit-data/pereval/?user__email=test1@test1.ru/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # проверяем что отбирается именно обьект со статусом for_test3
        self.assertEqual(response.json()[0]['title'], "for_test3")
