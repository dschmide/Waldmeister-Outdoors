import os
from django.contrib.gis.utils import LayerMapping
from .models import Vegetation

vegetation_mapping = {
    'ek72': 'EK72',
    'geom': 'MULTIPOLYGON25D',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), "../static/src/WALDVEGETATIONSKARTE_F_polygon.shp"))  # noqa


def run(verbose=True):
    print("loading shapefile")

    lm = LayerMapping(
        Vegetation, world_shp, vegetation_mapping,
        transform=True, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
