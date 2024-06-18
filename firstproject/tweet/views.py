from django.shortcuts import render
from .models import Tweet
from django.shortcuts import get_object_or_404,redirect
from .forms import TweetForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request,"index.html")

def show_tweets(request):
    query = request.GET.get('q',None)
    if query :
        tweets = Tweet.objects.filter(text__icontains=query).order_by("-created_at")
    else :
        tweets = Tweet.objects.all().order_by("-created_at")
    return render(request,"tweets.html",{"tweets" : tweets})

@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST , request.FILES)
        if form.is_valid() :
            tweetform = form.save(commit=False)
            tweetform.user = request.user
            tweetform.save()
            return redirect("tweets")
    else :
        form = TweetForm()
        return render(request,"create_tweet.html",{"form" : form })

@login_required
def edit_tweet(request,tweetid):
    print(type(tweetid))
    tweet = get_object_or_404(Tweet,pk=tweetid,user=request.user)
    print(tweet)
    if request.method=="POST":
        form = TweetForm(request.POST , request.FILES , instance=tweet)
        if form.is_valid() : 
            tweetform = form.save(commit=False)
            tweetform.user = request.user
            tweetform.save()
            return redirect("tweets")
    else :
        form = TweetForm(instance=tweet)
        return render(request,"create_tweet.html",{"form" : form })

@login_required  
def delete_tweet(request,tweetid):
    tweet = get_object_or_404(Tweet,pk=str(tweetid),user=request.user)
    if request.method == "POST" :
        tweet.delete()
        return redirect("tweets")
    return render(request,"delete_tweet.html" , {"tweet" : tweet})

def register(request):
    if request.method=="POST" :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect("tweets")
    else :
        form = UserRegistrationForm()
    return render(request,"registration/registration.html",{"form" : form})


