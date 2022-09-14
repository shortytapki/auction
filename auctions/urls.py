from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path('update_listings', views.update_listings, name="update_listings"),
    path("<int:listing_id>", views.show_particular_listing,
         name="show_particular_listing"),
    path('categories', views.categories, name="categories"),
    path('categories/<str:category>', views.show_particular_category,
         name="show_particular_category"),
    path('comment/<int:listing_id>', views.comment, name="comment")
]
