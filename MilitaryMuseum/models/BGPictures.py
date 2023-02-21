from django.db import models


class BGPictures(models.Model):
    picture = models.ImageField(max_length=100, upload_to="images/backgrounds/", verbose_name="Фоновое изображение")
    is_main_picture = models.BooleanField(verbose_name="Использовать как основную", default=True)

    class Meta:
        verbose_name_plural = 'Фоновые изображения сайта'
        verbose_name = 'Фоновое изображение сайта'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.is_main_picture:
            self.uncheck_main_picture()
        super().save()

    @staticmethod
    def uncheck_main_picture():
        query = BGPictures.objects.filter(is_main_picture=True).first()
        if query:
            query.is_main_picture = False
            query.save()

    @staticmethod
    def get_main_picture():
        query = BGPictures.objects.filter(is_main_picture=True).first()
        if query:
            return query.picture
        return None

    def __str__(self):
        return f"{self.picture} - {self.is_main_picture}"
