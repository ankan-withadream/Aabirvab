from django.db import models
from datetime import datetime

# Create your models here.
class Content(models.Model):
    CONTENT_TYPES = (
                        ("kobita", "kobita"),
                        ("golpo", "golpo"),
                        ("chobi", "chobi"),
                        ("cinemaReview", "cinemaReview"),
                        ("boiReview", "boiReview"),
                        ("rannaBanna", "rannaBanna"),
                        ("probondho", "probondho"),
                        ("boiBahar", "boiBahar"),
                        ("other", "other")
    )
    contentId = models.IntegerField(null=False, primary_key=True)
    contentType = models.CharField(null=False, max_length=12, choices=CONTENT_TYPES)
    contentAddingTime = models.DateTimeField(null=False)

class Kobita(models.Model):
    kobitaId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    kobitaText = models.TextField(null=False)
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class Golpo(models.Model):
    golpoId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    golpoText = models.TextField(null=False)
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class Chobi(models.Model):
    chobiId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    chobiField = models.ImageField(null=False, upload_to = "images")
    chobiText = models.TextField(null=False)
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class CinemaReview(models.Model):
    cinemaReviewId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    cinemaReviewText = models.TextField(null=False)
    cinemaReviewFile = models.FileField(null=False, upload_to = "cinema reviews")
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class BoiReview(models.Model):
    boiReviewId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    boiReviewText = models.TextField(null=False)
    boiReviewFile = models.FileField(null=False, upload_to = "boi reviews")
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class RannaBanna(models.Model):
    rannaBannaId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    rannaBannaText = models.TextField(null=False)
    rannaBannaFile = models.FileField(null=False, upload_to = "ranna bannas")
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class Probondho(models.Model):
    probondhoId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    probondhoText = models.TextField(null=False)
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class BoiBahar(models.Model):
    boiBaharId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    boiBaharText = models.TextField(null=False)
    boiBaharFile = models.FileField(null=False, upload_to = "books")
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)

class Other(models.Model):
    otherId = models.IntegerField(null=False, primary_key=True)
    contentId = models.ForeignKey("abirvab.Content", on_delete=models.CASCADE, default=0)
    otherText = models.TextField(null=False)
    otherFile = models.FileField(null=False, upload_to = "others")
    authorFirstName = models.CharField(max_length=15)
    authorLastName = models.CharField(max_length=15)


    
        #  1. Caption debo ki na, kivabe....done
        #  2. media rakhbo kothai ...done
        #  3. multiple media upload facility 