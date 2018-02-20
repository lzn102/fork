from django.shortcuts import render

from .models import Article
# Create your views here.


def index(request):
    detail = Article.objects.all()
    context = {"detail": detail}
    return render(request, "demo/index.html", context)