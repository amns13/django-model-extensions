from django.contrib import admin

from tests.testapp import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "created_at",
        "last_updated_at",
        "rating",
        "created_by",
        "last_updated_by",
    )


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "created_at",
        "last_updated_at",
        "created_by",
        "last_updated_by",
    )


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "created_at",
        "last_updated_at",
        "created_by",
        "last_updated_by",
    )


@admin.register(models.MediumType)
class MediumTypeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "created_at",
        "last_updated_at",
        "created_by",
        "last_updated_by",
    )


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "book",
        "medium",
        "created_at",
        "last_updated_at",
        "created_by",
        "last_updated_by",
    )


@admin.register(models.Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "created_at",
        "last_updated_at",
        "created_by",
        "last_updated_by",
    )


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "book",
        "score",
        "created_at",
        "last_updated_at",
        "created_by",
        "last_updated_by",
    )
