from django.db import models


class Record(models.Model):
    name = models.CharField(verbose_name='名前', max_length=30)
    note = models.TextField(
        verbose_name='メモ', max_length=400, null=True, blank=True)
    date = models.DateField(verbose_name='日付')
    image = models.ImageField(
        verbose_name='画像', upload_to='images/', null=True, blank=True)

    def get_absolute_url(self):
        return f"/records/{self.id}/"
