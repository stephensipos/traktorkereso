from django.db import models

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return self.description


class Tractor(models.Model):
    make = models.ForeignKey(Make, null=False, blank=False, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.DateField(null=True, blank=True)
    condition = models.ForeignKey(Condition, null=True, blank=True, on_delete=models.SET_NULL)
    hours = models.IntegerField(null=True, blank=True)
    engine_power = models.IntegerField(null=True, blank=True)
    documents_valid = models.DateField(null=True, blank=True)
    documents_type = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    url = models.CharField(max_length=2000, null=True, blank=True)
    fuel_type = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.make}_{self.model}_{self.id}".lower().replace(" ", "_")

class Equipment(models.Model):
    tractor = models.ForeignKey(Tractor, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tractor', 'name'], name='no duplicates')
        ]

