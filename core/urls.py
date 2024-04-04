from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

# router = SimpleRouter(trailing_slash=False)
# router.register("books", views.BookView, basename="books")
# router.register("books/<int:pk>", views.BookView, basename="book")
# urlpatterns = router.urls
app_name = "core_app"
urlpatterns = [
    path(
        "books",
        views.BookView.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="books",
    ),
    path(
        "books/<int:pk>",
        views.BookView.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="book",
    ),
    path("authors", views.AuthorView.as_view({"get": "list"}), name="authors"),
    path(
        "authors/<int:pk>",
        views.AuthorView.as_view({"get": "retrieve"}),
        name="author-detail",
    ),
    path("categories", views.CategoryView.as_view({"get": "list"}), name="categories"),
    path(
        "categories/<int:pk>",
        views.CategoryView.as_view({"get": "retrieve"}),
        name="category-detail",
    ),
]
