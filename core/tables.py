import django_tables2 as tables
from .models import Car, Charge, Order, Payment, Customer


class Table1(tables.Table):
    car_id = tables.Column(verbose_name='car_id')
    model = tables.Column(verbose_name='model')
    amount_of_places = tables.Column(verbose_name='amount_of_places')
    color = tables.Column(verbose_name='color')
    car_plate = tables.Column(verbose_name='car_plate')
    engineer = tables.Column(accessor='engineer.info.username', verbose_name='engineer_username')
    park = tables.Column(accessor='park.vid', verbose_name='park_id')

    # charging_station = tables.Column(accessor='charging_station.uid', verbose_name='Charging statiom')
    class Meta:
        model = Car
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table2(tables.Table):
    time = tables.Column(verbose_name='time')
    amount = tables.Column(verbose_name='amount')

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table3(tables.Table):
    percent = tables.Column(verbose_name='%')

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table4(tables.Table):
    id = tables.Column(verbose_name='id')
    order = tables.Column( verbose_name='order_id')
    time = tables.Column( verbose_name='time_of_payment')
    price = tables.Column(verbose_name='price')

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table5(tables.Table):
    avg_distance = tables.Column(verbose_name="Average distance")
    avg_duration = tables.Column(verbose_name="Average duration")

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table6(tables.Table):
    top_morning_1 = tables.Column(verbose_name="Top morning pick-up locations")
    top_afternoon_1 = tables.Column(verbose_name="Top afternoon pick-up locations")
    top_evening_1 = tables.Column(verbose_name="Top evening pick-up locations")

    top_morning_2 = tables.Column(verbose_name="Top morning destination")
    top_afternoon_2 = tables.Column(verbose_name="Top afternoon destination")
    top_evening_2 = tables.Column(verbose_name="Top evening destination")

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table7(tables.Table):
    car_id = tables.Column(verbose_name='car_id')
    model = tables.Column(verbose_name='model')
    amount_of_places = tables.Column(verbose_name='amount_of_places')
    color = tables.Column(verbose_name='color')
    car_plate = tables.Column(verbose_name='car_plate')
    engineer = tables.Column(accessor='engineer.info.username', verbose_name='engineer_username')
    park = tables.Column(accessor='park.vid', verbose_name='park_id')

    class Meta:
        model = Car
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table8(tables.Table):
    customer = tables.Column(verbose_name='customer')
    amount = tables.Column(verbose_name='amount')

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table9(tables.Table):
    workshop = tables.Column(verbose_name='workshop_id')
    amount = tables.Column(verbose_name='amount')

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'


class Table10(tables.Table):
    best = tables.Column(verbose_name='model')
    cost = tables.Column(verbose_name='cost')

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'
