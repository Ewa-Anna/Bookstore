import markdown

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from .models import Book


class LatestArrivals(Feed):
    title = "Bookstore"
    link = reverse_lazy("book:book_list")
    description = "New book arrivals in our store."

    def items(self):
        return Book.objects.all()[:5] 
    
    def item_title(self, item):
        return item.title
    
    def item_author(self, item):
        return item.author
    
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.description), 30)
    
    def item_pubdate(self, item):
        return item.created