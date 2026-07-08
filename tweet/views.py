from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

from .models import Tweet, Profile
from .forms import TweetForm, UserRegistrationForm, ProfileForm


def index(request):
    return render(request, "index.html")


def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet_list.html", {"tweets": tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")

    else:
        form = TweetForm()

    return render(request, "tweet_form.html", {"form": form})


@login_required
def tweet_edit(request, tweet_id):

    tweet = get_object_or_404(
        Tweet,
        pk=tweet_id,
        user=request.user
    )

    if request.method == "POST":

        form = TweetForm(
            request.POST,
            request.FILES,
            instance=tweet
        )

        if form.is_valid():
            form.save()
            return redirect("tweet_list")

    else:
        form = TweetForm(instance=tweet)

    return render(
        request,
        "tweet_form.html",
        {"form": form}
    )


@login_required
def tweet_delete(request, tweet_id):

    tweet = get_object_or_404(
        Tweet,
        pk=tweet_id,
        user=request.user
    )

    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")

    return render(
        request,
        "tweet_confirm_delete.html",
        {"tweet": tweet}
    )


def register(request):

    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("tweet_list")

    else:

        form = UserRegistrationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form
        }
    )


@login_required
def profile(request):

    profile = request.user.profile

    tweets = Tweet.objects.filter(
        user=request.user
    ).order_by("-created_at")

    tweet_count = tweets.count()

    return render(
        request,
        "profile.html",
        {
            "profile": profile,
            "tweets": tweets,
            "tweet_count": tweet_count,
        },
    )


@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect("profile")

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "edit_profile.html",
        {
            "form": form
        },
    )


def user_profile(request, username):

    user = get_object_or_404(
        User,
        username=username
    )

    profile = user.profile

    tweets = Tweet.objects.filter(
        user=user
    ).order_by("-created_at")

    tweet_count = tweets.count()

    return render(
        request,
        "profile.html",
        {
            "profile": profile,
            "tweets": tweets,
            "tweet_count": tweet_count,
            "profile_user": user,
        },
    )