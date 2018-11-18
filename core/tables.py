import django_tables2 as tables
from .models import Car

class CarTable(tables.Table):
    engineer = tables.Column(accessor='engineer.info.username')
    park = tables.Column(accessor='park.vid')
    charging_station = tables.Column(accessor='charging_station.uid')

    class Meta:
        model = Car
        template_name = 'django_tables2/bootstrap-responsive.html'
