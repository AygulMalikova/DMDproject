from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.query1, name='query1'),
    path('2/', views.query2, name='query2'),
    path('3/', views.query3, name='query3'),
    path('4/', views.query4, name='query4'),
    path('5/', views.query5, name='query5'),
    path('6/', views.query6, name='query6'),
    path('7/', views.query7, name='query7'),
    path('8/', views.query8, name='query8'),
    path('9/', views.query9, name='query9'),
    path('10/', views.query10, name='query10'),
]
