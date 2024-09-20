from django.contrib import admin

from .models import Post, Service


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author", "visible")
    search_fields = ("text", "author")
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "price", "for_main_page")
    search_fields = ("name",)
    empty_value_display = "-пусто-"
