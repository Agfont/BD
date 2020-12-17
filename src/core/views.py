from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
         
def list_conflicts(request):
    # i. Gerar um gráfico, histograma, por tipo de conflito e número de conflitos.
    records = models.Conflict.objects.raw(
        """
        select (
            select count(distinct(crel.conflito_id)) as total_conflitos_religiosos from ConfRelig creg
            select count(distinct(ceco.conflito_id)) as total_conflitos_economicos from ConfEcon ceco
            select count(distinct(creg.conflito_id)) as total_conflitos_regionais from ConfRegiao creg
            select count(distinct(cetn.conflito_id)) as total_conflitos_etnicos from ConfEtnia cetn
        ) as todos_conflitos;
        """
    )

    return {"data": records}


def dealers_and_armed_groups(request):
    # ii. Listar os traficantes e os grupos armados (Nome) para os quais os traficantes fornecem armas “Barret M82” ou “M200 intervention”.
    records = models.Dealer.objects.raw(
        """
        select t.nome_traficante, ga.nome_grupo
        from traficantes t
        join fornece f
        on f.id_traficante = t.id_traficante
        join grupos_armados ga
        on ga.id = f.codigo_grupo
        where fornece.nome_arma in ('Barret M82', 'M200 intervention')
        """
    )

    return {"data": records}

def top5_deads_conficts(request):
    # iii. Listar os 5 maiores conflitos em número de mortos.
    records = models.Conflict.objects.raw(
        """
        select * 
        from conflitos 
        order by num_mortos desc 
        limit 5;
        """
    )

    return {"data": records}

def top5_mediations_organizations(request):
    # iv. Listar as 5 maiores organizações em número de mediações.
    records = models.Organization.objects.raw(
        """
        select * 
        from organizacoes_m 
        inner join (
            select codigo_org, count(codigo_org) as mediacoes
            from enter_med
            group by enter_med.codigo_org
        ) mediacoes
        on organizacoes_m.codigo_org = mediations.codigo_org
        order by mediacoes desc
        limit 5;
        """
    )
    return {"data": records}

def top5_largest_armed_groups(request):
    # v. Listar os 5 maiores grupos armados com maior número de armas fornecidos.
    records = models.ArmedGroup.objects.raw(
        """
        select codigo_grupo, sum(num_armas) as total_armas
        from fornece
        group_by codigo_grupo
        order by total_armas desc
        limit 5;
        """
    )

    return {"data": records}

def countries_by_religious_conflicts(request):
    # vi. Listar o país e número de conflitos com maior número de conflitos religiosos.
    records = models.Conflict.objects.raw(
        """
        select creg.regiao, count(distinct(confitos.codigo)) codigo_conflito
        from conflitos
        inner join ConfRegiao creg 
        on conflitos.codigo = creg.conflito_id
        left join ConfRelig crel
        on conflitos.codigo = crel.conflito_id
        where crel.religiao is not NULL
        group by creg.regiao
        order by codigo_conflito desc
        limit 1
        """
    )