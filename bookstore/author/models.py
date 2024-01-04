from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    bio = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to="author_photos/%Y/%m/%d/", null=True, blank=True
    )
    own_url_page = models.URLField()
    email = models.EmailField(blank=True)
    birthdate = models.DateField(null=True, blank=True)

    slug = models.SlugField(default="", null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["surname"]
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["name", "surname"]),
            models.Index(fields=["created"]),
        ]

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_absolute_url(self):
        return reverse("author:author_detail", args=[self.slug])
