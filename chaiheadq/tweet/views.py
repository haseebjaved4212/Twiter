
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from .models import Tweet
# pyrefly: ignore [missing-import]
from .forms import TweetForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
# Create your views here. 


def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    
    return render(request, 'tweet_list.html', {'tweets': tweets})


# Create your new tweet
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet =  form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})


# Edit your existing tweet
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})


# Delete your existing tweet
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
