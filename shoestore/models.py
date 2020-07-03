from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=180)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=40)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'R'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    WHITE = 'WH'
    BLACK = 'BL'
    COLOR_NAME_CHOICES = [
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]
    color_name = models.CharField(max_length=2, choices=COLOR_NAME_CHOICES)

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    color = models.ForeignKey(
        ShoeColor,
        on_delete=models.CASCADE,
    )
    material = models.CharField(max_length=40)
    shoe_type = models.ForeignKey(
        ShoeType,
        on_delete=models.CASCADE
    )
    fasten_type = models.CharField(max_length=40)
