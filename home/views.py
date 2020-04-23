from django.shortcuts import render
from django.http import HttpResponse
from home.models import Post

# Create your views here.
def homepage(request):
    articoli = Post.objects.all()
    return render(request,'homepage.html', context=articoli)