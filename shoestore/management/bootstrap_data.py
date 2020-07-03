from django.core.management.base import BaseCommand
from shoestore.models import ShoeColor, ShoeType


class Command(BaseCommand):

    def handle(self, *args, **options):
        TYPE_NAME_CHOICES = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        for color in ShoeColor.COLOR_NAME_CHOICES:
            if not ShoeColor.objects.filter(color_name=color[0]):
                ShoeColor.objects.create(color_name=color[0])
                self.stdout.write(self.style.SUCCESS('Successfully added "%s"' % color[1]))
        for shoe_type in TYPE_NAME_CHOICES:
            if not ShoeType.objects.filter(style=shoe_type):
                ShoeType.objects.create(style=shoe_type)
                self.stdout.write(self.style.SUCCESS('Successfully added "%s"' % shoe_type))
