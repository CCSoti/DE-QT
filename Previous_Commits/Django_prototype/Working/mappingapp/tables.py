import django_tables2 as tables
from mappingapp.models import MappingappCoordinates


class CoordColumn(tables.Column):
    def render_elevation(self, value):
            if value == '12m':
                self.attrs = {"class": "red"}
            elif value == '61.0':
                self.attrs = {"class": "red"}


class CoordTable(tables.Table):

    class Meta:
        model = MappingappCoordinates
        # model.elevation = CoordColumn(accessor='tour.id_c_t.name_c', verbose_name='elevation')
        # add class="paleblue" to <table> tag
        # fields = ("id", "bng_ing", "grid_reference", "easting", "northing", "latitude", "longitude", "elevation")
        attrs = {"class": "paleblue"}

