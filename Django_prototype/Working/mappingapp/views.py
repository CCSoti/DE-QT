# from __future__ import unicode_literals
from datashape import null
import django
from django.db.models import Count, Aggregate, Avg, QuerySet
from django.shortcuts import render, render_to_response
from django_tables2 import RequestConfig

from chartit import DataPool, Chart, PivotChart, PivotDataPool
from mappingapp.models import MappingappCoordinates, MappingappOslSample
from mappingapp.tables import CoordTable


def graph(request):
    query = MappingappCoordinates.objects.values('latitude')
    latCount = MappingappCoordinates.objects.annotate(Count('latitude'))
    emptyQ = MappingappCoordinates.objects.none()
    latitude = []

    for w in query:
        dict = {}
        for key in w:
            if(w[key]!=None):
                dict[key] = w[key]
                latitude.append(dict)
    print (latitude)



    # return render_to_response('chart.html', {'coordinateschart': pivcht})


def coordinates(request):
    table = CoordTable(MappingappCoordinates.objects.all())
    # elevation_data = CoordTable(MappingappCoordinates.objects.filter(elevation='12m'))

    # context_dict = {"table": table, "elevation_data": elevation_data}
    RequestConfig(request).configure(table)
    return render(request, "coordinates.html", {"table": table})

