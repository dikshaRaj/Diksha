from django.contrib import admin

from home.models import Book,Author,Genre,Student


# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter=('name','purchase_date',('book_author',admin.RelatedOnlyFieldListFilter))
    list_filter=('name','purchase_date','book_author')
    search_fields=('id','name')
    fields=[('name','purchase_date'),('book_author','genre')]

    
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter=('author_name','total_book_written')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter=('name','book_name')

