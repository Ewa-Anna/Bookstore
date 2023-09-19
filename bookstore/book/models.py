from django.db import models


class Category(models.Model):
    catid = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cat_name}"


class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.URLField()
    slug = models.SlugField(default="", null=False)
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-title',]

    def __str__(self):
        return f"{self.title} by {self.author}"
