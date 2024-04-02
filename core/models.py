from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=["title"])]
