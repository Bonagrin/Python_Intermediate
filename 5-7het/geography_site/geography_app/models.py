from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    eu_member = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_capital = models.BooleanField()

    def __str__(self):
        return f"{self.name} ({self.country.name})"
    