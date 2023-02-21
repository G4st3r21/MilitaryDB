from django.db import models
from django.contrib.auth.models import User
from MilitaryMuseum.models.Ranks import Ranks


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.EmailField(blank=True, null=True, verbose_name="Почта")
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Имя")
    surname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество")
    is_admin = models.BooleanField(blank=True, null=True, verbose_name="Является глав. админом")

    def __unicode__(self):
        return self.user

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.is_admin:
            self.uncheck_admin()
        super().save()

    @staticmethod
    def get_admin_info():
        admin = UserProfile.objects.filter(is_admin=True).first()
        return {
            "fio": f"{admin.surname} {admin.name} {admin.patronymic}",
            "mail": admin.mail
        }

    @staticmethod
    def uncheck_admin():
        query = UserProfile.objects.filter(is_admin=True).first()
        if query:
            query.is_admin = False
            query.save()

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'
