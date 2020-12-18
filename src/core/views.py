from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms

from django.http import JsonResponse
from django.db import connection
from django.core import serializers
# from matplotlib import pyplot as plt
# from pandas import pandas as pd
import json

# Create your views here.

def conflict_form(request):
    
    form = forms.ConflictForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})


     
def military_chief_form(request):
    
    form = forms.MilitaryChiefForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def political_leader_form(request):
    
    form = forms.PoliticalLeaderForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})
     
def armed_group_form(request):
    
    form = forms.ArmedGroupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def division_form(request):
    
    form = forms.DivisionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def organization_form(request):
    
    form = forms.OrganizationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def weapon_form(request):
    
    form = forms.WeaponForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})

     
def dealer_form(request):
    
    form = forms.DealerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("FORM IS SAVED")

    return render(request, 'core/static/template/index.html', {'form': form})


# Create your views here.
def list_conflicts(request):
    cursor = connection.cursor()
    cursor.execute('''select tipo, count(distinct codigo) as quantidade
    from conflitos
    group by tipo
    order by tipo asc
    ''')


    records = cursor.fetchall()
    return HttpResponse(records)
    # # return render(records)
    # import matplotlib.pyplot as plt

    # x = []

    # for j in range(len(records)):
    #     for i in range(int(records[j][1])):
    #         x.append(records[j][0])

    # plt.hist(x, bins = 10)
    # plt.savefig('histogram.png')
    # plt.close()
    # try:
    #     with open('histogram.png', "rb") as f:
    #         return HttpResponse(f.read(), content_type="image/png")
    # except IOError:
    #     red = Image.new('RGBA', (1, 1), (255,0,0,0))
    #     response = HttpResponse(content_type="image/png")
    #     red.save(response, "JPEG")
    #     return response


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
CREATE OR REPLACE FUNCTION exclusividade_confTerritorial() RETURN TRIGGER AS $territorial$
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

CREATE TRIGGER conflito_economico BEFORE INSERT OR UPDATE on "ConfRegiao"
FOR EACH ROW EXECUTE PROCEDURE exclusividade_confTerritorial();

-- Étnico
CREATE OR REPLACE FUNCTION exclusividade_confEtnico() RETURN TRIGGER AS $etnico$
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

CREATE TRIGGER conflito_economico BEFORE INSERT OR UPDATE on "ConfRegiao"
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
|   id := (SELECT MAX(divisao_id)
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

    return HttpResponse(records)