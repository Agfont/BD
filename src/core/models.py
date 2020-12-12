# from django.db import models

# # Create your models here.
# class PoliticalLeader(models.Model):
#     name = models.CharField()
#     support = models.CharField()
#     military_chief = models.ManyToManyField()

# # Table lideres_politicos as lp {
# #   id int [pk, increment] // auto-increment
# #   nome_l varchar
# #   apoios varchar
# #   codigo_chefe_militar varchar [ref: < cm.codigo_chef]
# # }

# # Table grupos_armados_lideres_politicos {
# #   grupo_armado_id int [ref: > ga.codigo_g]
# #   lider_politico_id int [ref: > lp.id] 
 
# # Table lideres_politicos_organizacoes_m {
# #   lider_politico_id int [ref: > lp.id] 
# #   organizacoes_id int [ref: > om.codigo_org]
# #  }
# #  }

# class MilitaryChief(models.Model):
#     rank = models.CharField()

# # Table chefes_militares as cm {
# #   codigo_chef int [pk]
# #   faixa varchar 
# #  }

# # Table divisoes_chefes_militares { //colocar limite de 1 a 3?
# #   divisao_id int [ref: > d.nro_divisao]
# #   chefe_militar_id int [ref: > cm.codigo_chef] 
# #  }
 
# class Organization(models.Model):
#     name = models.CharField()
#     sort = models.CharField()
#     amount = models.IntegerField()

 
# # Table organizacoes_m as om {
# #   codigo_org int [pk]
# #   nome_org varchar
# #   tipo_ajuda varchar //enum!
# #   num_pessoas int
# #   tipo char
# #  }
 
# # Table organizacoes_organizacoes { //é assim que faz?
# #   organizacao_mae_id int [ref: - om.codigo_org]
# #   organizacoes_filha_id int [ref: > om.codigo_org]
# #  }
 
# # Table divisoes as d{
# #   nro_divisao int [pk]
# #   num_baixas_d int
# #   barcos int
# #   tanques int
# #   avioes int
# #   homens int
# # }

# # Table grupos_armados as ga{
# #   codigo_g int [pk]
# #   nome_grupo varchar 
# #   num_baixas_g int
# #   divisao_nro int [ref: < d.nro_divisao]
# # }

# # Table conflitos as c{
# #   codigo int [pk]
# #   nome varchar 
# #   pais varchar
# #   num_mortos int 
# #   num_feridos int
# #   sort varchar
# # }

# # Table conflitos_grupos_armados {
# #   grupo_armado_id int [ref: > ga.codigo_g]
# #   conflito_id int [ref: > c.codigo]
# #   de_grupo timestamp
# #   ds_grupo timestamp
# #  }
 
# # Table conflitos_organizacoes {
# #   conflito_id int [ref: > c.codigo]
# #   organizacao_id int [ref: > om.codigo_org]
# #   de_media timestamp
# #   ds_media timestamp
# #  }
 
# # Table tipo_armas as ta {
# #   nome_arma var [pk]
# #   indicador int 
# # }

# class Dealer(models.Model):
#     #(unique=True) #(primary_key=True) ??
#     name = models.CharField()

# # Table traficantes as t {
# #   nome_traf var [pk]
# # }

# # Table tipo_armas_traficantes {
# #   nome_arma var [ref: > ta.nome_arma]
# #   nome_traf var [ref: > t.nome_traf]
# #   quantidade int
# # }

# # Table grupos_armados_tipo_armas {
# #   grupo_armado_id int [ref: > ga.codigo_g]
# #   tipo_arma_id int [ref: > ta.nome_arma]
# #   traficante_id int [ref: > t.nome_traf]
# #   num_armas int
# #  }

