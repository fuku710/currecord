from django.db import models


class Model(models.Model):
    name = models.CharField(verbose_name='名前', max_length=30)
    note = models.TextField(verbose_name='メモ', max_length=400, null=True)
    date = models.DateField(verbose_name='日付')