from main.models import Coards, PerevalAdd, PerevalImages
from rest_framework import serializers



class CoardsSerializer(serializers.ModelSerializer):
    """координаты перевала"""


    class Meta:
        model = Coards
        # exclude = (id,)
        # fields = ("latitude", "longitude", "height")
        fields = ("beautyTitle",
                  "title",
                  "other_titles",
                  "connect",
                  "coards",
                  "level_winter",
                  "level_summer",
                  "level_autumn",
                  "level_spring",
                  )


class PerevalsSerializer(serializers.ModelSerializer):
    """список перевалов"""

    # coards = serializers.PrimaryKeyRelatedField(queryset=Coards.objects.all())

    class Meta:
        model = PerevalAdd
        fields = (
            # "beautyTitle",
            "id",
            "status",
            "title",
            # "other_titles",
            # "connect",
            # "coards_id",
            # "level_winter",
            # "level_summer",
            # "level_autumn",
            # "level_spring",
        )


class PerevalSerializer(serializers.ModelSerializer):
    """детализация перевала"""

    class Meta:
        model = PerevalAdd
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    """Фотограии перевала"""

    class Meta:
        model = PerevalImages
        fields = "__all__"


class PhotoAddSerializer(serializers.ModelSerializer):
    """Фотограии перевала"""

    img = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = PerevalImages
        fields = (
            "img",
            "title",
            "date_added",
            "pereval"
        )