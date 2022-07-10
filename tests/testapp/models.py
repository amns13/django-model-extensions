from django.db import models

from django_model_extensions.models import CreatedUpdatedTimestampModel


class Publication(CreatedUpdatedTimestampModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Rating(CreatedUpdatedTimestampModel):
    score = models.FloatField()

    def __str__(self) -> str:
        return str(self.pk)


class Genre(CreatedUpdatedTimestampModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class MediumType(CreatedUpdatedTimestampModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(CreatedUpdatedTimestampModel):
    title = models.CharField(max_length=255)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    rating = models.OneToOneField(
        Rating, on_delete=models.SET_NULL, null=True, blank=True
    )
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    mediums = models.ManyToManyField(MediumType, through="testapp.Price")

    def __str__(self) -> str:
        return self.title


class Price(CreatedUpdatedTimestampModel):
    medium = models.ForeignKey(MediumType, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return str(self.pk)


class Author(CreatedUpdatedTimestampModel):
    name = models.CharField(max_length=255, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.name
