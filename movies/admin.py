from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Genre, Movie

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') #list_display is a reserved name for defining what to show

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'numbers_in_stock', 'daily_rate')
    exclude = ('date_created',) #same here, exclude is a reserved word

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)