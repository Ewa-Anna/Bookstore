from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


class Category(models.Model):
    catid = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['cat_name']
        indexes = [models.Index(fields=['cat_name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.cat_name}"


class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.URLField()
    available = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False)
    created = models.DateTimeField(auto_now_add=True)
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TaggableManager()

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=['bookid', 'slug']), 
                   models.Index(fields=["title"]), 
                   models.Index(fields=["author"]), 
                   models.Index(fields=['-created'])]

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("book:book_detail", args=[self.slug])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["book"]), models.Index(fields=["name"])]

    def __str__(self):
        return f"Review added by {self.name} for book {self.book}"
