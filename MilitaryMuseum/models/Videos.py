from django.db import models
from .Combatants import Combatants


class Videos(models.Model):
    video = models.FileField(max_length=100, upload_to="videos/", verbose_name="Видео")
    combatant = models.ForeignKey(Combatants, on_delete=models.CASCADE, verbose_name="Документ")

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f"{self.combatant.name}"
