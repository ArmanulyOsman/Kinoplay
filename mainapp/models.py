from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField(upload_to='images/')


class Category(models.Model):
    name = models.CharField(max_length=30)


class Movie(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/')
    rating = models.IntegerField()
    year = models.IntegerField()
    video = models.FileField(upload_to='movies/')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='director')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movie'


