from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import JsonResponse
from django.db import connection
from django.core import serializers
from matplotlib import pyplot as plt
from pandas import pandas as pd
import json

# Create your views here.
def list_conflicts(request):
    cursor = connection.cursor()
    cursor.execute('''select tipo, count(distinct codigo) as quantidade
    from conflitos
    group by tipo
    order by tipo asc
    ''')


    records = cursor.fetchall()

    import matplotlib.pyplot as plt

    x = []

    for j in range(len(records)):
        for i in range(int(records[j][1])):
            x.append(records[j][0])

    plt.hist(x, bins = 10)
    plt.savefig('histogram.png')
    plt.close()
    try:
        with open('histogram.png', "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/png")
        red.save(response, "JPEG")
        return response


def dealers_and_armed_groups(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT traficantes.nome_traficante as traficante, grupos_armados.nome_grupo as grupo, nome_arma as arma
                        FROM fornece 
                        JOIN traficantes ON fornece.id_traficante = traficantes.id_traficante
                        JOIN grupos_armados ON fornece.codigo_grupo = grupos_armados.id
                        WHERE nome_arma = 'Barret M82' OR nome_arma = 'M200 intervention';
    ''')

    x = []

    for i in cursor:
        x.append({'traficate': i[0], 'grupo': i[1], 'arma': i[2]})

    return JsonResponse(x,safe=False)

def top5_deads_conficts(request):
    cursor = connection.cursor()
    cursor.execute(
        """
        select * 
        from conflitos 
        order by num_mortos desc 
        limit 5;
        """
    )

    x = []

    for i in cursor:
        x.append({'conflito': i[1], 'mortos': i[4]})

    return JsonResponse(x,safe=False)

def top5_mediations_organizations(request):
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT nome_org, COUNT(*) as num_intermed
        FROM organizacoes_m
        JOIN "EntraMed" ON organizacoes_m.codigo_org = "EntraMed".codigo_org
        GROUP BY "EntraMed".codigo_org, organizacoes_m.codigo_org
        ORDER BY num_intermed DESC LIMIT 5;
        """
    )
    
    x = []

    for i in cursor:
        x.append({'organização': i[0], 'intermediação': i[1]})

    return JsonResponse(x,safe=False)

def top5_largest_armed_groups(request):
    # v. Listar os 5 maiores grupos armados com maior número de armas fornecidos.
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT grupos_armados.nome_grupo, SUM(num_armas) as total
        FROM fornece
        join grupos_armados on fornece.codigo_grupo = grupos_armados.id
        GROUP BY grupos_armados.nome_grupo
        ORDER BY total DESC LIMIT 5;
        """
    )

    x = []

    for i in cursor:
        x.append({'grupo': i[0], 'armas': i[1]})

    return JsonResponse(x,safe=False)

def countries_by_religious_conflicts(request):
    # vi. Listar o país e número de conflitos com maior número de conflitos religiosos.
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT regiao, COUNT(conflito_id) as conflitos
        FROM "ConfRegiao"
        GROUP BY regiao
        ORDER BY conflitos DESC limit 1;
        """
    )

    x = []

    for i in cursor:
        x.append({'pais': i[0], 'conflitos': i[1]})

    return JsonResponse(x,safe=False)

def test(request):
    return JsonResponse({'log': 'We are online!'})

def addMilitaryChief(request):
    return HttpResponse('ok')