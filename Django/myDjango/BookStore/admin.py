from django.contrib import admin
from .models import Book , BookReview, BookStore, BookAuthor

class BookReviewInline(admin.TabularInline):
    model = BookReview
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'stream',)
    inlines = [BookReviewInline]

class BookStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('books',)

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'bio',)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(BookStore, BookStoreAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)