from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms

from django.http import JsonResponse
from django.db import connection
from django.core import serializers
from matplotlib import pyplot as plt
from pandas import pandas as pd


# Create your views here.
def populate(request):
    cursor = connection.cursor()
    cursor.execute('''
    --12
    INSERT INTO public.grupos_armados (id, nome_grupo, num_baixas) VALUES (2, 'grupo armado 2', 12321);
    INSERT INTO public.grupos_armados (id, nome_grupo, num_baixas) VALUES (3, 'grupo armado 3', 3123);
    INSERT INTO public.grupos_armados (id, nome_grupo, num_baixas) VALUES (4, 'grupo armado 4', 12312);
    INSERT INTO public.grupos_armados (id, nome_grupo, num_baixas) VALUES (1, 'grupo armado 1', 223);
    --13
    INSERT INTO public.lideres_politicos (id, codigo_grupo, nome_l, apoios) VALUES (1, 1, 'Arthur', 'Apoios');
    INSERT INTO public.lideres_politicos (id, codigo_grupo, nome_l, apoios) VALUES (2, 2, 'Gabriel', 'Apoios');
    INSERT INTO public.lideres_politicos (id, codigo_grupo, nome_l, apoios) VALUES (3, 3, 'Victor', 'Apoios');
    INSERT INTO public.lideres_politicos (id, codigo_grupo, nome_l, apoios) VALUES (4, 4, 'Mateus', 'Apoios');
    --1
    INSERT INTO public.chefes_militares (codigo_chef, faixa, n_div, id_lider, codigo_grupo) VALUES (1, 'Faixa', 1, 1, 1);
    INSERT INTO public.chefes_militares (codigo_chef, faixa, n_div, id_lider, codigo_grupo) VALUES (2, 'Faixa', 1, 2, 2);
    INSERT INTO public.chefes_militares (codigo_chef, faixa, n_div, id_lider, codigo_grupo) VALUES (4, 'Faixa', 4, 4, 4);
    INSERT INTO public.chefes_militares (codigo_chef, faixa, n_div, id_lider, codigo_grupo) VALUES (3, 'Faixa', 1, 2, 2);
    --4
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (14, 'conflito 13', 'Territorial', 1312313, 123123);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (17, 'conflito 17', 'Econômico', 1312313, 45568);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (7, 'conflito 6', 'Territorial', 1312313, 234234);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (4, 'conflito 4', 'Territorial', 1312313, 7675);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (1, 'conflito 1', 'Étnico', 1312313, 12334);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (16, 'conflito 16', 'Econômico', 1312313, 978);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (10, 'conflito 9', 'Religioso', 1312313, 213);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (3, 'conflito 3', 'Étnico', 1312313, 3455);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (18, 'conflito 18', 'Econômico', 1312313, 789);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (2, 'conflito 2', 'Religioso', 113123, 345);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (11, 'conflito 10', 'Econômico', 1312313, 32);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (6, 'conflito 14', 'Religioso', 1312313, 123);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (5, 'conflito 5', 'Econômico', 1312313, 56734534);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (13, 'conflito 12', 'Territorial', 1312313, 123);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (15, 'conflito 15', 'Econômico', 1312313, 123);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (12, 'conflito 11', 'Étnico', 1312313, 132);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (8, 'conflito 7', 'Religioso', 1312313, 123);
    INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (9, 'conflito 8', 'Territorial', 1312313, 312);               
    --5
    INSERT INTO public."ConfRegiao" (conflito_id, regiao) VALUES (1, 'reg 1');
    INSERT INTO public."ConfRegiao" (conflito_id, regiao) VALUES (2, 'reg 1');
    INSERT INTO public."ConfRegiao" (conflito_id, regiao) VALUES (3, 'reg 2');
    INSERT INTO public."ConfRegiao" (conflito_id, regiao) VALUES (4, 'reg 3');
    INSERT INTO public."ConfRegiao" (conflito_id, regiao) VALUES (5, 'reg 3');
    --14
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (1, 'org 1', 'tipo ajuda', 20, 'a', 'b');
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (2, 'org 2', 'tipo ajuda', 20, 'a', 'b');
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (3, 'org 3', 'tipo ajuda', 20, 'a', 'b');
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (4, 'org 4', 'tipo ajuda', 20, 'a', 'b');
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (5, 'org 5', 'tipo ajuda', 20, 'a', 'b');
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (6, 'org 6', 'tipo ajuda', 20, 'a', 'b');
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (7, 'org 7', 'tipo ajuda', 20, 'a', 'b');
    INSERT INTO public.organizacoes_m (codigo_org, nome_org, tipo_ajuda, num_pessoas, tipo, org_lider) VALUES (8, 'org 8', 'tipo ajuda', 20, 'a', 'b');
    --8
    INSERT INTO public.divisoes (divisao_id, codigo_grupo, num_baixas_d, barcos, tanques, avioes, homens) VALUES (1, 1, 123, 1, 13, 123, 112313);
    --9
    INSERT INTO public."EntPart" (grupo_armado_id, conflito_id, de_grupo) VALUES (1, 1, '2020-12-16 23:27:23.000000');
    INSERT INTO public."EntPart" (grupo_armado_id, conflito_id, de_grupo) VALUES (2, 1, '2020-12-16 23:27:44.000000');
    --10
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (1, 1, '2020-12-17 19:04:17.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (1, 1, '2020-12-17 19:04:42.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (2, 2, '2020-12-17 19:04:43.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (2, 3, '2020-12-17 19:04:43.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (3, 5, '2020-12-17 19:04:44.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (1, 6, '2020-12-17 19:04:44.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (2, 7, '2020-12-17 19:04:45.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (3, 8, '2020-12-17 19:04:45.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (4, 9, '2020-12-17 19:04:46.000000');
    INSERT INTO public."EntraMed" (codigo_org, conflito_id, de_media) VALUES (1, 4, '2020-12-17 19:04:44.000000');
    --17
    INSERT INTO public.tipo_armas (nome_arma, indicador) VALUES ('M200 intervention', 1);
    INSERT INTO public.tipo_armas (nome_arma, indicador) VALUES ('Barret M82', 2);
    --18
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (1, 'traficante 1');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (2, 'traficante 2');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (3, 'traficante 3');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (4, 'traficante 4');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (5, 'traficante 5');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (6, 'traficante 6');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (7, 'traficante 7');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (8, 'traficante 8');
    INSERT INTO public.traficantes (id_traficante, nome_traficante) VALUES (9, 'traficante 9');
    --11
    INSERT INTO public.fornece (codigo_grupo, nome_arma, id_traficante, num_armas) VALUES (3, 'M200 intervention', 1, 123);
    INSERT INTO public.fornece (codigo_grupo, nome_arma, id_traficante, num_armas) VALUES (2, 'M200 intervention', 2, 12333);
    INSERT INTO public.fornece (codigo_grupo, nome_arma, id_traficante, num_armas) VALUES (4, 'Barret M82', 2, 3457);
    INSERT INTO public.fornece (codigo_grupo, nome_arma, id_traficante, num_armas) VALUES (1, 'Barret M82', 1, 13);
    ''')
    
    return HttpResponse("O BD foi populado!")

def conflict_form(request):
    form = forms.ConflictForm()    
    if request.method == 'POST':
        form = forms.ConflictForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})


     
def military_chief_form(request):
    form = forms.MilitaryChiefForm()    
    if request.method == 'POST':
        form = forms.MilitaryChiefForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def political_leader_form(request):
    form = forms.PoliticalLeaderForm()    
    if request.method == 'POST':
        form = forms.PoliticalLeaderForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})
     
def armed_group_form(request):
    form = forms.ArmedGroupForm()    
    if request.method == 'POST':
        form = forms.ArmedGroupForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def division_form(request):
    form = forms.DivisionForm()    
    if request.method == 'POST':
        form = forms.DivisionForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def organization_form(request):
    form = forms.OrganizationForm()    
    if request.method == 'POST':
        form = forms.OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def weapon_form(request):
    form = forms.WeaponForm()        
    if request.method == 'POST':
        form = forms.WeaponForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def dealer_form(request):
    form = forms.DealerForm()    
    if request.method == 'POST':
        form = forms.DealerForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})



def submit_form(request):
    x = []

    for i in request.POST.values():
        x.append(i)

    
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO public.conflitos (codigo, nome, tipo, num_feridos, num_mortos) VALUES (%i, %s, %s, %i, %i);"
        %(int(x[1]),x[2],x[3],int(x[4]),int(x[5]))
        )

    return HttpResponse("Conflito inserido")

# Create your views here.
def list_conflicts(request):
    cursor = connection.cursor()
    cursor.execute('''select tipo, count(distinct codigo) as quantidade
    from conflitos
    group by tipo
    order by tipo asc
    ''')


    x = []

    for i in cursor:
        for j in range(i[1]):
            x.append(i[0])

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

    # return HttpResponse(records)
    return JsonResponse(x,safe=False)

def drop_schema(request):
    cursor = connection.cursor()
    cursor.execute('''DROP schema public CASCADE''')
    cursor.execute('''CREATE schema public''')
    return HttpResponse("Esquema foi criado novamente")


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

    # return HttpResponse(records)
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
    # return HttpResponse(records)
    
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

    # return HttpResponse(records)
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
    return render(request,'core/static/template/home.html')

def addMilitaryChief(request):
    return HttpResponse('ok')


def create_db(request):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE "grupos_armados" (
  "id" int NOT NULL PRIMARY KEY,
  "nome_grupo" varchar,
  "num_baixas" int
);
-- PoliticalLeader
create TABLE "lideres_politicos" (
  "id" int NOT NULL UNIQUE ,
  "codigo_grupo" int,
  "nome_l" varchar,
  "apoios" varchar,
  PRIMARY KEY("id","codigo_grupo"),
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id")
);
-- MilitaryChief
CREATE TABLE "chefes_militares" (
  "codigo_chef" int NOT NULL PRIMARY KEY,
  "faixa" varchar,
  "n_div" int,
  "id_lider" int NOT NULL,
  "codigo_grupo" int,
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("id_lider") REFERENCES "lideres_politicos" ("id")
);


-- Division
CREATE TABLE "divisoes" (
  "divisao_id" int NOT NULL,
  "codigo_grupo" int NOT NULL,
  "num_baixas_d" int,
  "barcos" int,
  "tanques" int,
  "avioes" int,
  "homens" int,
  PRIMARY KEY("divisao_id", "codigo_grupo"),
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id")
);
-- Organization
CREATE TABLE "organizacoes_m" (
  "codigo_org" int NOT NULL PRIMARY KEY,
  "nome_org" varchar,
  "tipo_ajuda" varchar,
  "num_pessoas" int,
  "tipo" char,
  "org_lider" char
);
-- Conflict
CREATE TABLE "conflitos" (
  "codigo" int NOT NULL PRIMARY KEY,
  "nome" varchar,
  "tipo" varchar,
  "num_feridos" int,
  "num_mortos" int
);
-- Weapon
CREATE TABLE "tipo_armas" (
  "nome_arma" varchar NOT NULL PRIMARY KEY,
  "indicador" int
);
-- Dealer
CREATE TABLE "traficantes" (
  "id_traficante" int NOT NULL PRIMARY KEY,
  "nome_traficante" varchar
);
-- SupplyWeaponArmedGroupDealer
CREATE TABLE "fornece" (
  "codigo_grupo" int NOT NULL,
  "nome_arma" varchar NOT NULL,
  "id_traficante" int NOT NULL,
  "num_armas" int,
  PRIMARY KEY("codigo_grupo", "nome_arma", "id_traficante"),
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("nome_arma") REFERENCES "tipo_armas" ("nome_arma"),
  FOREIGN KEY ("id_traficante") REFERENCES "traficantes" ("id_traficante")
);

-- DialogPoliticalLeaderArmedGroupOrganization
CREATE TABLE "dialoga" (
  "codigo_lider" int NOT NULL,
  "codigo_grupo" int NOT NULL,
  "organizacoes_id" int NOT NULL,
  PRIMARY KEY("codigo_lider", "codigo_grupo", "organizacoes_id"),
  FOREIGN KEY ("codigo_lider") REFERENCES "lideres_politicos" ("id"),
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("organizacoes_id") REFERENCES "organizacoes_m" ("codigo_org")
);
-- EnterPart
CREATE TABLE "EntPart" (
  "grupo_armado_id" int NOT NULL,
  "conflito_id" int NOT NULL,
  "de_grupo" timestamp NOT NULL,
  PRIMARY KEY("grupo_armado_id", "conflito_id", "de_grupo"),
  FOREIGN KEY ("grupo_armado_id") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
-- ExitPart
CREATE TABLE "SaidaPart" (
  "grupo_armado_id" int NOT NULL,
  "conflito_id" int NOT NULL,
  "ds_grupo" timestamp NOT NULL,
  PRIMARY KEY("grupo_armado_id", "conflito_id", "ds_grupo"),
  FOREIGN KEY ("grupo_armado_id") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
-- EnterMed
CREATE TABLE "EntraMed" (
  "codigo_org" int NOT NULL,
  "conflito_id" int NOT NULL,
  "de_media" timestamp NOT NULL,
  PRIMARY KEY("codigo_org", "conflito_id", "de_media"),
  FOREIGN KEY ("codigo_org") REFERENCES "organizacoes_m" ("codigo_org"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
-- ExitMed
CREATE TABLE "SaidaMed" (
  "codigo_org" int NOT NULL,
  "conflito_id" int NOT NULL,
  "ds_media" timestamp NOT NULL,
  PRIMARY KEY("codigo_org", "conflito_id", "ds_media"),
  FOREIGN KEY ("codigo_org") REFERENCES "organizacoes_m" ("codigo_org"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
-- CanSupply
CREATE TABLE "PodeFornecer" (
  "nome_arma" varchar,
  "id_traficante" int,
  "quantidade" int,
  FOREIGN KEY ("nome_arma") REFERENCES "tipo_armas" ("nome_arma"),
  FOREIGN KEY ("id_traficante") REFERENCES "traficantes" ("id_traficante")
);
CREATE TABLE "ConfRelig" (
  "conflito_id" int NOT NULL,
  "religiao" varchar NOT NULL,
  PRIMARY KEY ("conflito_id", "religiao"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "ConfEcon" (
  "conflito_id" int NOT NULL,
  "mat_prima" varchar NOT NULL,
  PRIMARY KEY ("conflito_id", "mat_prima"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "ConfRegiao" (
  "conflito_id" int NOT NULL,
  "regiao" varchar NOT NULL,
  PRIMARY KEY ("conflito_id", "regiao"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);

CREATE TABLE "ConfEtnia" (
  "conflito_id" int NOT NULL,
  "etnia" varchar NOT NULL,
  PRIMARY KEY ("conflito_id", "etnia"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);

-- 1.a)
-- Religioso
CREATE OR REPLACE FUNCTION exclusividade_confRelig() RETURNS TRIGGER AS $relig$
BEGIN
    IF EXISTS(SELECT conflito_id FROM "ConfEcon"
              WHERE conflito_id = NEW.conflito_id) THEN
         RAISE EXCEPTION 'Erro: O conflito % já é do tipo econômico.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfRegiao"
              WHERE conflito_id = NEW.conflito_id) THEN
         RAISE EXCEPTION 'Erro: O conflito % já é do tipo territorial.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfEtnia"
              WHERE conflito_id = NEW.conflito_id) THEN
         RAISE EXCEPTION 'Erro: O conflito % já é do tipo étnico.', NEW.conflito_id;
    END IF;
    RETURN NEW;
END;
$relig$
LANGUAGE plpgsql;

CREATE TRIGGER conflito_religioso BEFORE INSERT OR UPDATE on "ConfRelig"
FOR EACH ROW EXECUTE PROCEDURE exclusividade_confRelig();

-- Econômico
CREATE OR REPLACE FUNCTION exclusividade_confEcon() RETURNS TRIGGER AS $econ$
BEGIN
    IF EXISTS(SELECT conflito_id FROM "ConfRelig"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo religioso.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfRegiao"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo territorial.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfEtnia"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo étnico.', NEW.conflito_id;
    END IF;
    RETURN NEW;
END;
$econ$
LANGUAGE plpgsql;

CREATE TRIGGER conflito_economico BEFORE INSERT OR UPDATE on "ConfEcon"
FOR EACH ROW EXECUTE PROCEDURE exclusividade_confEcon();

-- Territorial
CREATE OR REPLACE FUNCTION exclusividade_confTerritorial() RETURNS TRIGGER AS $territorial$
BEGIN
    IF EXISTS(SELECT conflito_id FROM "ConfRelig"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo religioso.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfEcon"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo econômico.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfEtnia"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo étnico.', NEW.conflito_id;
    END IF;
    RETURN NEW;
END;
$territorial$
LANGUAGE plpgsql;

CREATE TRIGGER conflito_territorial BEFORE INSERT OR UPDATE on "ConfRegiao"
FOR EACH ROW EXECUTE PROCEDURE exclusividade_confTerritorial();

-- Étnico
CREATE OR REPLACE FUNCTION exclusividade_confEtnico() RETURNS TRIGGER AS $etnico$
BEGIN
    IF EXISTS(SELECT conflito_id FROM "ConfRelig"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo religioso.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfEcon"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo econômico.', NEW.conflito_id;
    ELSIF EXISTS(SELECT conflito_id FROM "ConfRegiao"
            WHERE conflito_id = NEW.conflito_id) THEN
        RAISE EXCEPTION 'Erro: O conflito % já é do tipo territorial.', NEW.conflito_id;
    END IF;
    RETURN NEW;
END;
$etnico$
LANGUAGE plpgsql;

CREATE TRIGGER conflito_etnico BEFORE INSERT OR UPDATE on "ConfRegiao"
FOR EACH ROW EXECUTE PROCEDURE exclusividade_confEtnico();

-- 1.b)
-- Tabela chefes_militares: "id_lider" int NOT NULL
-- Também criamos uma tabela adicional caso um chefe tenha mais de um líder

-- 1.c)
CREATE OR REPLACE FUNCTION divisao_min_1_chefe() returns trigger AS $divisaoMin1$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        IF (SELECT COUNT(codigo_chef) FROM chefes_militares
            WHERE n_div = OLD.n_div) = 1 THEN
            RAISE EXCEPTION 'Erro: A divisão % é dirigida apenas pelo chefe %.', old.n_div, old.codigo_chef;
        END IF;
        RETURN OLD;
    ELSIF (SELECT COUNT(codigo_chef) FROM chefes_militares
        WHERE n_div = OLD.n_div) = 1 AND NEW.n_div != OLD.n_div THEN
        RAISE EXCEPTION 'Erro: A divisão % é dirigida apenas pelo chefe %.', old.n_div, old.codigo_chef;
    END IF;
    RETURN NEW;
END;
$divisaoMin1$
LANGUAGE plpgsql;

CREATE TRIGGER minimo_chefes BEFORE DELETE OR UPDATE ON chefes_militares
FOR EACH ROW EXECUTE PROCEDURE divisao_min_1_chefe();

-- 1.d)
CREATE OR REPLACE FUNCTION divisao_max_3_chefes() returns trigger AS $divisaoMax3$
BEGIN
    IF ((SELECT COUNT(codigo_chef) FROM chefes_militares
        WHERE n_div = NEW.n_div) = 3
        AND TG_OP = 'UPDATE'
        AND NEW.n_div != OLD.n_div )THEN
        RAISE EXCEPTION 'Erro: A divisão % já é dirigida por 3 chefes .', new.n_div;

    ELSIF (SELECT COUNT(codigo_chef) FROM chefes_militares
        WHERE n_div = NEW.n_div) = 3  THEN
        RAISE EXCEPTION 'Erro: A divisão % já é dirigida por 3 chefes .', new.n_div;
    END IF;
    RETURN NEW;
END;
$divisaoMax3$
LANGUAGE plpgsql;

CREATE TRIGGER maximo_chefes BEFORE INSERT OR UPDATE ON chefes_militares
FOR EACH ROW EXECUTE PROCEDURE divisao_max_3_chefes();

-- 1.e)
CREATE OR REPLACE FUNCTION grupo_min_1_div() returns trigger AS $grupoMinDiv$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        IF (SELECT COUNT(divisao_id) FROM divisoes
            WHERE codigo_grupo = OLD.codigo_grupo) = 1 THEN
            RAISE EXCEPTION 'Erro: Todo grupo dispõe de no mínimo 1 divisão.';
        END IF;
        RETURN OLD;

    ELSIF ((SELECT COUNT(divisao_id) FROM divisoes
            WHERE codigo_grupo = OLD.codigo_grupo) = 1
            AND NEW.codigo_grupo != OLD.codigo_grupo) THEN
        RAISE EXCEPTION 'Erro: Todo grupo dispõe de no mínimo 1 divisão.';
    END IF;
    RETURN NEW;
END;
$grupoMinDiv$
LANGUAGE plpgsql;

CREATE TRIGGER min1_div_grupo BEFORE DELETE OR UPDATE ON divisoes
FOR EACH ROW EXECUTE PROCEDURE grupo_min_1_div();



-- 1.f)
CREATE OR REPLACE FUNCTION conflito_min_2_grupos() returns trigger AS $conflito2Grupos$
DECLARE grupos_part int;
BEGIN
    grupos_part := (SELECT COUNT(DISTINCT grupo_armado_id)
                    FROM "EntPart"
                    group by  conflito_id);
    IF grupos_part <= 2 THEN
    RAISE EXCEPTION '"Erro: Em um conflito participam no mínimo 2 grupos armados.';
    END IF;
    RETURN OLD;
END;
$conflito2Grupos$
LANGUAGE plpgsql;

CREATE TRIGGER conflito_2_grupos BEFORE DELETE ON "EntPart"
FOR EACH ROW EXECUTE PROCEDURE conflito_min_2_grupos();

-- 1.g)
CREATE OR REPLACE FUNCTION conflito_min_1_pais() returns trigger AS $conflito1Pais$
BEGIN
    IF TG_OP = 'DELETE' AND
        (SELECT COUNT(*) FROM "ConfRegiao"
        WHERE regiao = OLD.regiao) = 1 THEN
        RAISE EXCEPTION 'Erro: Qualquer conflito afeta pelo menos 1 país.';
    END IF;
    RETURN NEW;
END;
$conflito1Pais$
LANGUAGE plpgsql;

CREATE TRIGGER conflito_paises BEFORE DELETE OR UPDATE ON "ConfRegiao"
FOR EACH ROW EXECUTE PROCEDURE conflito_min_1_pais();

-- 1.h
CREATE OR REPLACE FUNCTION num_baixas() returns trigger AS $novasBaixas$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        UPDATE grupos_armados
        SET num_baixas = num_baixas + NEW.num_baixas_d
        WHERE grupos_armados.id = NEW.codigo_grupo;
        RETURN NEW;
    ELSIF (TG_OP = 'UPDATE') THEN
        UPDATE grupos_armados
        SET num_baixas = num_baixas + NEW.num_baixas_d - OLD.num_baixas_d
        WHERE grupos_armados.id = NEW.codigo_grupo;
        RETURN NEW;

    ELSE
        UPDATE grupos_armados
        SET num_baixas = num_baixas - OLD.num_baixas_d
        WHERE grupos_armados.id = OLD.codigo_grupo;
        RETURN OLD;
    END IF;
    RETURN NEW;
END;
$novasBaixas$
LANGUAGE plpgsql;

CREATE TRIGGER atualizar_baixas AFTER INSERT OR DELETE OR UPDATE ON divisoes
FOR EACH ROW EXECUTE PROCEDURE num_baixas();

--1.h - Parte 2)
CREATE OR REPLACE FUNCTION id_divisoes() returns trigger AS $idDiv$
DECLARE id int;
BEGIN
   id := (SELECT MAX(divisao_id)
        FROM divisoes
        WHERE codigo_grupo = NEW.codigo_grupo
        GROUP BY divisao_id, codigo_grupo);
    IF id IS NULL THEN
        NEW.divisao_id := 1;
    ELSE
        NEW.divisao_id := id + 1;
    END IF;
    RETURN NEW;
END;
$idDiv$
LANGUAGE plpgsql;

CREATE TRIGGER atualizar_id_div BEFORE INSERT ON divisoes
FOR EACH ROW EXECUTE PROCEDURE id_divisoes();
        """
    )
    return HttpResponse("O banco de dados foi criado!")

    # return HttpResponse(records)
