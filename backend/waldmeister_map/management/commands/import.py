from django.core.management.base import BaseCommand
import os
from django.contrib.gis.utils import LayerMapping
from waldmeister_map.models import Vegetation


class Command(BaseCommand):
    help = 'This command imports the VegetationLayer data'

    def handle(self, *args, **options):
        vegetation_mapping = {
            'ek72': 'EK72',
            'geom': 'MULTIPOLYGON25D',
        }
        world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../static/src/WALDVEGETATIONSKARTE_F_polygon.shp"))  # noqa

        Vegetation.objects.all().delete()

        lm = LayerMapping(
            Vegetation, world_shp, vegetation_mapping,
            transform=True, encoding='iso-8859-1',
        )
        lm.save(strict=True, verbose=True)
