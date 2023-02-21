from django.db import models

from MilitaryMuseum.models.Ranks import Ranks
from MilitaryMuseum.models.Places import Places


class Combatants(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=70, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=70, verbose_name="Отчество", blank=True)
    rank = models.ForeignKey(Ranks, verbose_name="Звание", blank=True, null=True, on_delete=models.CASCADE)
    battalion = models.CharField(max_length=100, verbose_name="Батальон", blank=True)
    issue_year = models.IntegerField(verbose_name="Год выпуска", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    date_of_death = models.DateField(verbose_name="Дата смерти", blank=True, null=True)
    place_of_birth = models.ForeignKey(
        Places, verbose_name="Место рождения",
        blank=True, null=True,
        on_delete=models.CASCADE
    )
    details = models.TextField(verbose_name="Подробности", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Документы'
        verbose_name = 'Документ'

    @staticmethod
    def get_all_ranks():
        return set(combatant.rank for combatant in Combatants.objects.all())

    def get_fio(self):
        if self.patronymic:
            return f"{self.surname} {self.name} {self.patronymic}"
        else:
            return f"{self.surname} {self.name}"

    def __str__(self):
        return f"{self.name} {self.surname} - {self.rank}"
