from django.db import models
from django.urls import reverse


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
        ordering = ['title']
        indexes = [
            models.Index(fields=['title'])
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse('book:book_detail',
                       args=[self.slug])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['book']),
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return f"Review added by {self.name} for book {self.book}"