from django.contrib import admin

from books.models import Book, Author, BookAuthor, Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')
    search_fields = ('title', 'isbn')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name' )
    search_fields = ('first_name', 'last_name' )

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
    search_fields = ('book', 'author')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'comment')
    search_fields = ('book', 'user', 'comment')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(Review, ReviewAdmin)