from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Item(models.Model):
    create_data = models.DateField()
    summary = models.CharField(max_length=50, verbose_name="Заголовок", unique=True, null=False, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,
                               default=1, related_name="projects", verbose_name="Автор")
    def __str__(self):
        return f"{self.id} {self.summary}"

    class Meta:
        db_table = "Items"
        verbose_name = "Новость"
        verbose_name_plural = "Новость"

