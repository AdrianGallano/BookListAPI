from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [models.Index(fields=["name"])]

class Author(models.Model):
    name = models.CharField(max_length=255)
    no_of_books_published = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=["name"])]


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField(default=0)
    author = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="category_book")

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=["title"])]

