from django.db import models

from django_model_extensions.models import (
    CreatedUpdatedByModel,
    CreatedUpdatedTimestampModel,
    CreatedUpdatedTimeUserModel,
)


class Publication(CreatedUpdatedTimeUserModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Rating(CreatedUpdatedTimeUserModel):
    score = models.FloatField()

    def __str__(self) -> str:
        return str(self.pk)


class Genre(CreatedUpdatedTimeUserModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class MediumType(CreatedUpdatedTimeUserModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(CreatedUpdatedTimeUserModel):
    title = models.CharField(max_length=255)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    rating = models.OneToOneField(
        Rating, on_delete=models.SET_NULL, null=True, blank=True
    )
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    mediums = models.ManyToManyField(MediumType, through="testapp.Price")

    def __str__(self) -> str:
        return self.title


class Price(CreatedUpdatedTimeUserModel):
    medium = models.ForeignKey(MediumType, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return str(self.pk)


class Author(CreatedUpdatedTimeUserModel):
    name = models.CharField(max_length=255, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.name


class CreatedUpdatedTimestampTestModel(CreatedUpdatedTimestampModel):
    pass


class CreatedUpdatedByTestModel(CreatedUpdatedByModel):
    pass
