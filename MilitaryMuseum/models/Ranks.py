from django.db import models


class Ranks(models.Model):
    rank = models.CharField(max_length=100, verbose_name="Звание")

    class Meta:
        verbose_name_plural = "Звания"
        verbose_name = "Звание"

    @staticmethod
    def get_all_ranks():
        return set(place.place for place in Ranks.objects.all())

    def __str__(self):
        return f"{self.rank}"
