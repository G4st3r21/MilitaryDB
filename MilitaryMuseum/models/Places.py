from django.db import models


class Places(models.Model):
    place = models.CharField(max_length=100, verbose_name="Место")

    class Meta:
        verbose_name_plural = "Места рождения"
        verbose_name = "Места"

    @staticmethod
    def get_all_places():
        return set(place.place for place in Places.objects.all())

    def __str__(self):
        return f"{self.place}"
