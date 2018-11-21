import django_tables2 as tables
from .models import Car, Charge

class CarTable(tables.Table):
    car_id = tables.Column(verbose_name='car_id')
    model = tables.Column(verbose_name='model')
    amount_of_places = tables.Column(verbose_name='amount_of_places')
    car_plate = tables.Column(verbose_name='car_plate')
    color = tables.Column(verbose_name='color')
    # park = tables.Column(accessor='park.vid', verbose_name='park_id')
    engineer = tables.Column(accessor='engineer.info.username', verbose_name='engineer_id')
    park = tables.Column(accessor='park.vid', verbose_name='park_id')

    # charging_station = tables.Column(accessor='charging_station.uid', verbose_name='Charging statiom')

    class Meta:
        model = Car
        template_name = 'django_tables2/bootstrap-responsive.html'


class ChargeTable(tables.Table):
    class Meta:
        model = Charge
        template_name = 'django_tables2/bootstrap-responsive.html'
