from django.db import models
from users.models import User

status_choices = [
    ("new", "новый"),
    ("pending", "модератор взял в работу"),
    ("accepted", "модерация прошла успешно"),
    ("rejected", "модерация прошла, информация не принята"),
]


class PerevalAdd(models.Model):
    title = models.CharField(max_length=255)
    beautyTitle = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()
    # coards = models.OneToOneField(Coards, on_delete=models.CASCADE)

    level_winter = models.CharField(max_length=255)
    level_summer = models.CharField(max_length=255)
    level_autumn = models.CharField(max_length=255)
    level_spring = models.CharField(max_length=255)

    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    status = models.CharField(max_length=10, choices=status_choices, default="new")
    date_added = models.DateField(auto_now_add=True)
    add_time = models.TimeField(auto_now_add=True)
    users = models.ManyToManyField(User, through='PerevalUser')

    def __str__(self):
        return f"id: {self.pk}, title:{self.title}"


class PerevalUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pu_user")
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE, related_name="pereval")

    def __str__(self):
        return f"id: {self.pk}, username:{self.user}"


class PerevalAreas(models.Model):
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE, related_name="areas")
    title = models.TextField()


class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE, related_name="photos")
    title = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return f"id: {self.pk}, title:{self.title}"
