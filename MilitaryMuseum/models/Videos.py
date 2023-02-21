from django import forms
from django.core.validators import FileExtensionValidator
from django.db import models
from .Combatants import Combatants


class Videos(models.Model):
    video = models.FileField(
        max_length=100, upload_to="videos/", verbose_name="Видео",
        validators=[FileExtensionValidator(allowed_extensions=["mp4", "webm", "ogg"])],
    )
    combatant = models.ForeignKey(Combatants, on_delete=models.CASCADE, verbose_name="Документ")

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f"{self.combatant.name}"
