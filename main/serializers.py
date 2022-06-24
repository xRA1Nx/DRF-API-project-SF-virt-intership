from main.models import Coards, PerevalAdd, PerevalImages, User, PerevalUser
from rest_framework import serializers


class CoardsSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = PerevalAdd
        fields = "__all__"


class PhotoDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = "__all__"


class PhotoAddSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = PerevalImages
        fields = (
            "img",
            "title",
            "date_added",
            "pereval"
        )


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class UserDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "fname", "lname")


class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class PerevalUserSerializer:
    

    class Meta:
        model = PerevalUser
        fields = "__all__"
