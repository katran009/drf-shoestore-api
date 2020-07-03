from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from shoestore.models import Shoe, ShoeType, ShoeColor, Manufacturer


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'url')


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('id', 'color_name',)


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style',)


class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'id',
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type',
        )
