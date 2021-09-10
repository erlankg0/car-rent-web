from django.db import models


class Team(models.Model):
    photo = models.ImageField(upload_to='photos_team/%Y/%m/%d')
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    designation = models.CharField(verbose_name='Профессия', max_length=255)
    facebook_link = models.URLField(unique=True, max_length=200)
    twitter_link = models.URLField(unique=True, max_length=200)
    google_plus_link = models.URLField(unique=True, max_length=200)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
