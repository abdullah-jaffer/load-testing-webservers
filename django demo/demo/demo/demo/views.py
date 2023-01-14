from django.core import serializers
from django.http import JsonResponse

from demo.demo.models import Book
from demo.demo.serializers import BookSerializer

def get_book(self):
    book = Book("Domain Driven Design", "AL35202111090000000001234567", 426)
    return JsonResponse(book.toJSON(), safe=False)
