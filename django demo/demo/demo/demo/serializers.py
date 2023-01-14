from rest_framework import serializers
from demo.demo.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'IBAN', 'pages']