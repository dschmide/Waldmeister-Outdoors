from django.apps import AppConfig
# import os
# from django.contrib.gis.gdal import DataSource
# from waldmeister_map import load


class WaldmeisterMapConfig(AppConfig):
    name = 'waldmeister_map'

    def ready(self):
        pass
