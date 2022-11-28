# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Models
from .models import Book


class IndexView(generic.ListView):
    """
    **Question list**

    This view render a list of questions published until _today_ in descending order of published date.

    Model: **Book**

    Template: **book/index.html**

    Context:

    - **book_list**: alias for default list.
    """
    model = Book
    template_name = "book/index.html"
    context_object_name = "book_list"


class DetailView(generic.DetailView):
    """
    **Book detailed**

    This view render a detailed book.

    Model: **Book**

    Template: **book/detail.html**
    """
    model = Book
    template_name = "book/detail.html"
