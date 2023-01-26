from django.db import models


class Combatants(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=70, verbose_name="Фамилия")
    rank = models.CharField(max_length=70, verbose_name="Звание", null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", null=True)
    date_of_death = models.DateField(verbose_name="Дата смерти", null=True)
    native_city = models.CharField(max_length=50, verbose_name="Родной город", null=True)
    details = models.TextField(verbose_name="Подробности", null=True)

    class Meta:
        verbose_name_plural = 'Документы'
        verbose_name = 'Документ'

    def __str__(self):
        return f"{self.name} {self.surname} - {self.rank}"


class Pictures(models.Model):
    picture = models.CharField(max_length=100, verbose_name="Название изображения")
    combatant = models.ForeignKey(Combatants, on_delete=models.CASCADE, verbose_name="Документ")

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'

    def __str__(self):
        return f"{self.combatant.name}"

# class Movies(models.Model):
#     movie = models.CharField(max_length=100)
#     combatant = models.ManyToManyField
