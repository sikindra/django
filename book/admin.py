from csv import list_dialects
from django.contrib import admin
from django.contrib.admin.sites import site
from book.models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_des', 'book_image', 'book_slug')

admin.site.register(Book,BookAdmin)
# Register your models here.
