from django.shortcuts import render

def author_list(request):
    return render(request, "list.html")

def author_detail(request, slug):
    return render(request, "detail.html")