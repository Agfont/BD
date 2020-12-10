CREATE TABLE "chefes_militares" (
  "codigo_chef" int PRIMARY KEY,
  "faixa" varchar, 
  "n_div" int,
  "codigo_grupo" int,
  "codigo_lider" int,
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("codigo_lider") REFERENCES "lideres_politicos" ("id")
);
CREATE TABLE "lideres_politicos" (
  "id" int,
  "codigo_grupo" int,
  "nome_l" varchar,
  "apoios" varchar,
  PRIMARY KEY("id","codigo_grupo"), 
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id")
);
CREATE TABLE "grupos_armados" (
  "id" int PRIMARY KEY,
  "nome_grupo" varchar,
  "num_baixas" int
);
CREATE TABLE "divisoes" (
  "divisao_id" int,
  "codigo_grupo" int,
  "num_baixas_d" int,
  "barcos" int,
  "tanques" int,
  "avioes" int,
  "homens" int,
  PRIMARY KEY("divisao_id", "codigo_grupo"),
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id")
);
CREATE TABLE "organizacoes_m" (
  "codigo_org" int PRIMARY KEY,
  "nome_org" varchar,
  "tipo_ajuda" varchar,
  "num_pessoas" int,
  "tipo" char,
  "org_lider" char
);
CREATE TABLE "conflitos" (
  "codigo" int PRIMARY KEY,
  "nome" varchar,
  "tipo" varchar,
  "num_feridos" int,
  "num_mortos" int
);
CREATE TABLE "tipo_armas" (
  "nome_arma" varchar PRIMARY KEY,
  "indicador" int
);
CREATE TABLE "traficantes" (
  "id_traficante" int PRIMARY KEY,
  "nome_traficante" varchar
);
CREATE TABLE "fornece" (
  "codigo_grupo" int,
  "nome_arma" varchar,
  "id_traficante" int,
  "num_armas" int,
  PRIMARY KEY("codigo_grupo", "nome_arma", id_traficante),
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("nome_arma") REFERENCES "tipos_armas" ("nome_arma"),
  FOREIGN KEY ("id_traficante") REFERENCES "traficantes" ("id_traficante")
);
CREATE TABLE "dialoga" (
  "codigo_lider" int,
  "codigo_grupo" int,
  "organizacoes_id" int,
  PRIMARY KEY("codigo_lider", "codigo_grupo", "organizacoes_id"),
  FOREIGN KEY ("codigo_lider") REFERENCES "lideres_politicos" ("id"),
  FOREIGN KEY ("codigo_grupo") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("organizacoes_id") REFERENCES "organizacoes_m" ("codigo_org")
);
CREATE TABLE "EntPart" (
  "grupo_armado_id" int,
  "conflito_id" int,
  "de_grupo" timestamp,
  PRIMARY KEY("grupo_armado_id", "conflito_id", "de_grupo"),
  FOREIGN KEY ("grupo_armado_id") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "SaidaPart" (
  "grupo_armado_id" int,
  "conflito_id" int,
  "ds_grupo" timestamp,
  PRIMARY KEY("grupo_armado_id", "conflito_id", "ds_grupo"),
  FOREIGN KEY ("grupo_armado_id") REFERENCES "grupos_armados" ("id"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "EntraMed" (
  "codigo_org" int,
  "conflito_id" int,
  "de_media" timestamp,
  PRIMARY KEY("codigo_org", "conflito_id", "de_media"),
  FOREIGN KEY ("codigo_org") REFERENCES "organizacoes_m" ("codigo_org"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "SaidaMed" (
  "codigo_org" int,
  "conflito_id" int,
  "ds_media" timestamp,
  PRIMARY KEY("codigo_org", "conflito_id", "ds_media")
  FOREIGN KEY ("codigo_org") REFERENCES "organizacoes_m" ("codigo_org"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "PodeFornecer" (
  "nome_arma" varchar,
  "id_traficante" int,
  "quantidade" int,
  FOREIGN KEY ("id_traficante") REFERENCES "traficantes" ("id_traficante")
);
CREATE TABLE "ConfRelig" (
  "conflito_id" int,
  "religiao" varchar,
  PRIMARY KEY ("conflito_id", "religiao"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "ConfEcon" (
  "conflito_id" int,
  "mat_prima" varchar,
  PRIMARY KEY ("conflito_id", "mat_prima"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "ConfRegiao" (
  "conflito_id" int,
  "regiao" varchar,
  PRIMARY KEY ("conflito_id", "regiao"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "ConfPais" (
  "conflito_id" int,
  "pais" varchar,
  PRIMARY KEY ("conflito_id", "pais"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);
CREATE TABLE "ConfEtnia" (
  "conflito_id" int,
  "etnia" varchar,
  PRIMARY KEY ("conflito_id", "etnia"),
  FOREIGN KEY ("conflito_id") REFERENCES "conflitos" ("codigo")
);

/*
CREATE TABLE "chefes_lider" (
  "codigo_chef" int,
  "codigo_lider" int
);
CREATE RULE chefMin1Lider AS 
     ON DELETE TO chefes_lider ( (SELECT COUNT(DINSTINCT codigo_lider) FROM chefes_lider)>= 1 );
     DO INSTEAD NOTHING;

CREATE RULE divMin1Max3Chefs AS 
     ON DELETE TO chefes_lider ( (SELECT COUNT(DINSTINCT codigo_lider) FROM chefes_lider)>= 1 );
     DO INSTEAD NOTHING;
*/
