from asyncio.windows_events import NULL
from cgitb import text
from turtle import pos, title
from unicodedata import category
from urllib import request
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    return render(request, "auctions/create_listing.html")


def update_listings(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category', '')
        bid = request.POST.get('bid')
        url = request.POST.get('url')
        new_listing = Listing(
            title=title, description=description, category=category, starting_bid=bid, image_url=url, listed_by=request.user)
        new_listing.save()
        return HttpResponseRedirect(reverse('index'))


def show_particular_listing(request, listing_id):
    post = Listing.objects.get(id=listing_id)
    return render(request, "auctions/listing_page.html", {
        "listing": post,
        "comments": Comment.objects.filter(post=post)
    })


def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Listing.objects.values('category').distinct()
    })


def show_particular_category(request, category):
    return render(request, "auctions/category_page.html", {
        "listings": Listing.objects.filter(category=category),
        "category": category
    })


def comment(request, listing_id):
    if request.method == "POST":
        post = Listing.objects.get(pk=listing_id)
        author = request.user
        text = request.POST.get('text')
        new_comment = Comment(author=author, text=text, post=post)
        new_comment.save()
        return HttpResponseRedirect(f'/{listing_id}')
