from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Item(models.Model):
    create_data = models.DateField()
    summary = models.CharField(max_length=50, verbose_name="Заголовок", unique=True, null=False, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,
                               default=1, related_name="items", verbose_name="Автор")


    def __str__(self):
        return f"{self.id} {self.summary}"

    class Meta:
        db_table = "Items"
        verbose_name = "Новость"
        verbose_name_plural = "Новость"

class Users(User):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=False, blank=False, upload_to='avatars', verbose_name='Аватар')

    def str(self):
        return self.user.username

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_data = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey('webapp.Item', related_name='items', on_delete=models.CASCADE,
                                verbose_name='Тема')

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
