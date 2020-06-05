from django.contrib import admin
from .models import Post, Comment, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "title", "description")
    # добавляем интерфейс для поиска по тексту
    list_filter = ("title",)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text")
    list_filter = ("created",)
    empty_value_display = '-пусто-'


# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Group, GroupAdmin)