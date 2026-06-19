from django.shortcuts import render
# pyrefly: ignore [missing-import]
from .models import Tweet
# pyrefly: ignore [missing-import]
from .forms import TweetForm
from django.shortcuts import get_object_or_404
# Create your views here. 


def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    
    return render(request, 'tweet_list.html', {'tweets': tweets})