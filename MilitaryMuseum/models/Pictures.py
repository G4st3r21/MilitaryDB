from django.db import models
from .Combatants import Combatants


class Pictures(models.Model):
    picture = models.ImageField(max_length=100, upload_to="images/combatants/", verbose_name="Изображение")
    is_main_picture = models.BooleanField(verbose_name="Является главной фотографией", default=False)
    combatant = models.ForeignKey(Combatants, on_delete=models.CASCADE, verbose_name="Документ")

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'

    def __str__(self):
        return f"{self.combatant.name}"
