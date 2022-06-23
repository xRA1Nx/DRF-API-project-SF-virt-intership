from main.models import Coards, PerevalAdd
from rest_framework import serializers


class CoardsSerializer(serializers.ModelSerializer):
    """координаты перевала"""

    class Meta:
        model = Coards
        # exclude = (id,)
        # fields = ("latitude", "longitude", "height")
        fields = "__all__"


class PerevalAddSerializer(serializers.ModelSerializer):
    """координаты перевала"""

    class Meta:
        model = PerevalAdd
        # fields = "__all__"
        fields = ("beautyTitle",
                  "title",
                  "other_titles",
                  "connect",
                  "coards_id",
                  "level_winter",
                  "level_summer",
                  "level_autumn",
                  "level_spring",
                  )
