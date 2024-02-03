from .models import Category


def categories(request):
    category_object = Category.objects.all()
    return {"categories": category_object}
