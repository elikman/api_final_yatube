from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts', verbose_name='Автор')
    image = models.ImageField(upload_to='posts/', blank=True,
                              verbose_name='Изображение')
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True,
                              blank=True, related_name='posts',
                              verbose_name='Группа')

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments', verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', verbose_name='Пост')
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField('Дата добавления', auto_now_add=True,
                                   db_index=True)

    class Meta:
        default_related_name = 'comments'


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower',
                             verbose_name='Пользователь')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following',
                                  verbose_name='Автор')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='unique_followers')
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.following}'


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название группы')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
