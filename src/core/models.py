from django.db import models

# Create your models here.
CHARFIELD_LENGTH = 100

class MilitaryChief(models.Model):
    class Meta:
        db_table = 'chefes_militares'

    codigo_chef = models.IntegerField(primary_key=True)
    faixa = models.CharField(max_length=CHARFIELD_LENGTH)
    n_div = models.IntegerField()
    id_lider = models.ForeignKey('PoliticalLeader', on_delete=models.CASCADE)
    codigo_grupo = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)

class PoliticalLeader(models.Model):
    class Meta:
        db_table = 'lideres_politicos'
     
    nome_l = models.CharField(max_length=CHARFIELD_LENGTH)
    codigo_grupo = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE, db_column='codigo_grupo')
    apoios = models.CharField(max_length=CHARFIELD_LENGTH)

class ArmedGroup(models.Model):
    class Meta:
        db_table = 'grupos_armados'

    nome_grupo = models.CharField(max_length=CHARFIELD_LENGTH, null=False, blank=False)
    num_baixas = models.IntegerField()

class Division(models.Model):
    class Meta:
        db_table = 'divisoes'
        
    divisao_id = models.IntegerField(primary_key=True)
    codigo_grupo = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    num_baixas_d = models.IntegerField()
    barcos = models.IntegerField()
    tanques = models.IntegerField()
    avioes = models.IntegerField()
    homens = models.IntegerField()

class Organization(models.Model):
    class Meta:
        db_table = 'organizations'
        
    nome_org = models.CharField(max_length=CHARFIELD_LENGTH)
    tipo = models.CharField(max_length=CHARFIELD_LENGTH)
    num_pessoas = models.IntegerField()
    tipo_ajuda = models.CharField(max_length=CHARFIELD_LENGTH)
    org_lider = models.CharField(max_length=CHARFIELD_LENGTH)

class Conflict(models.Model):
    class Meta:
        db_table = 'conflitos'

    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=CHARFIELD_LENGTH)
    tipo = models.CharField(max_length=CHARFIELD_LENGTH)
    num_feridos = models.IntegerField()
    num_mortos = models.IntegerField()


class Weapon(models.Model):
    class Meta:
        db_table = 'tipo_armas'

    nome_arma = models.CharField(max_length=CHARFIELD_LENGTH, primary_key=True)
    indicador = models.IntegerField()

class Dealer(models.Model):
    class Meta: 
        db_table = 'traficantes'

    id_traficante = models.IntegerField(primary_key=True)
    nome_traficante = models.CharField(max_length=CHARFIELD_LENGTH)

class SupplyWeaponArmedGroupDealer(models.Model):
    class Meta:
        db_table = 'fornece'

    codigo_grupo = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    nome_arma = models.ForeignKey('Weapon', on_delete=models.CASCADE)
    id_traficante = models.ForeignKey('Dealer', on_delete=models.CASCADE)
    num_armas = models.IntegerField()

class DialogPoliticalLeaderArmedGroupOrganization(models.Model):
    class Meta:
        db_table = 'dialoga'

    codigo_lider = models.ForeignKey('PoliticalLeader', on_delete=models.CASCADE)
    codigo_grupo = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    organizacoes_id = models.ForeignKey('Organization', on_delete=models.CASCADE)

class EnterPart(models.Model):
    class Meta:
        db_table = 'EntPart'

    grupo_armado_id = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflito_id = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    de_grupo = models.DateField(auto_now=False)

class ExitPart(models.Model):
    class Meta:
        db_table = 'SaidaPart'

    grupo_armado_id = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflito_id = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    ds_grupo = models.DateField(auto_now=False)
    
class EnterMed(models.Model):
    class Meta:
        db_table = 'EntraMed'

    codigo_org = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflito_id = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    de_media = models.DateField(auto_now=False)

class ExitMed(models.Model):
    class Meta:
        db_table = 'SaidaMed'

    codigo_org = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflito_id = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    ds_media = models.DateField(auto_now=False)

class CanSupply(models.Model):
    class Meta:
        db_table = 'PodeFornecer'

    nome_arma = models.ForeignKey('Weapon', on_delete=models.CASCADE)
    id_traficante = models.ForeignKey('Dealer', on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Religious(models.Model):
    class Meta:
        db_table = 'ConfRelig'

    conflito_id = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    religiao = models.CharField(null=False , max_length=50)

class Economic(models.Model):
    class Meta:
        db_table = 'ConfEcon'

    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    mat_prima = models.CharField(null=False , max_length=50)
    

class Region(models.Model):
    class Meta:
        db_table = 'ConfRegiao'

    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    regiao = models.CharField(null=False , max_length=50)

class Etnic(models.Model):
    class Meta:
        db_table = 'ConfEtnia'

    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    etnia = models.CharField(null=False , max_length=50)


class PoliticalLeadersMilitaryChiefs(models.Model):
    class Meta:
        db_table = 'lideres_politicos_chefes_militares'

    political_leader = models.ForeignKey('PoliticalLeader', on_delete=models.CASCADE)
    military_chief = models.ForeignKey('MilitaryChief', on_delete=models.CASCADE)


# '''        
# //// -- LEVEL 1
# //// -- Tables and References

# // Creating tables
# Table lideres_politicos as lp {
#   id int [pk, increment] // auto-increment
#   nome_l varchar
#   apoios varchar
#   codigo_chefe_militar varchar [ref: < cm.codigo_chef]
# }

# Table grupos_armados_lideres_politicos {
#   grupo_armado_id int [ref: > ga.codigo_g]
#   lider_politico_id int [ref: > lp.id] 
#  }
 
# Table lideres_politicos_organizacoes_m {
#   lider_politico_id int [ref: > lp.id] 
#   organizacoes_id int [ref: > om.codigo_org]
#  }

# Table chefes_militares as cm {
#   codigo_chef int [pk]
#   faixa varchar 
#  }
 
 
# Table divisoes_chefes_militares { //colocar limite de 1 a 3?
#   divisao_id int [ref: > d.nro_divisao]
#   chefe_militar_id int [ref: > cm.codigo_chef] 
#  }
 
# Table organizacoes_m as om {
#   codigo_org int [pk]
#   nome_org varchar
#   tipo_ajuda varchar //enum!
#   num_pessoas int
#   tipo char
#  }
 
# Table organizacoes_organizacoes { //é assim que faz?
#   organizacao_mae_id int [ref: - om.codigo_org]
#   organizacoes_filha_id int [ref: > om.codigo_org]
#  }
 
# Table divisoes as d{
#   nro_divisao int [pk]
#   num_baixas_d int
#   barcos int
#   tanques int
#   avioes int
#   homens int
# }

# Table grupos_armados as ga{
#   codigo_g int [pk]
#   nome_grupo varchar 
#   num_baixas_g int
#   divisao_nro int [ref: < d.nro_divisao]
# }

# Table conflitos as c{
#   codigo int [pk]
#   nome varchar 
#   pais varchar
#   num_mortos int 
#   num_feridos int
#   tipo varchar
# }

# Table regioes{
#   codigo int [ref: < c.codigo]
#   regiao varchar
# }

# Table religioes{
#   codigo int [ref: < c.codigo]
#   religiao varchar
# }

# Table mat_primas{
#   codigo int [ref: < c.codigo]
#   mat_prima varchar
# }

# Table etnias {
#   codigo int [ref: < c.codigo]
#   etnia varchar
# }

# Table conflitos_grupos_armados {
#   grupo_armado_id int [ref: > ga.codigo_g]
#   conflito_id int [ref: > c.codigo]
#   de_grupo timestamp
#   ds_grupo timestamp
#  }
 
# Table conflitos_organizacoes {
#   conflito_id int [ref: > c.codigo]
#   organizacao_id int [ref: > om.codigo_org]
#   de_media timestamp
#   ds_media timestamp
#  }
 
# Table tipo_armas as ta {
#   nome_arma var [pk]
#   indicador int 
# }

# Table traficantes as t {
#   nome_traf var [pk]
# }

# Table tipo_armas_traficantes {
#   nome_arma var [ref: > ta.nome_arma]
#   nome_traf var [ref: > t.nome_traf]
#   quantidade int
# }

# Table grupos_armados_tipo_armas {
#   grupo_armado_id int [ref: > ga.codigo_g]
#   tipo_arma_id int [ref: > ta.nome_arma]
#   traficante_id int [ref: > t.nome_traf]
#   num_armas int
#  }



# //--------------------------------------------------------------------------//
# //--------------------------------------------------------------------------//
# //--------------------------------------------------------------------------//
# //--------------------------------------------------------------------------//
# //--------------------------------------------------------------------------//
# //--------------------------------------------------------------------------//
# //--------------------------------------------------------------------------//
# //--------------------------------------------------------------------------//
# // Creating references
# // You can also define relaionship separately
# // > many-to-one; < one-to-many; - one-to-one

# //----------------------------------------------//

# //// -- LEVEL 2
# //// -- Adding column settings

# // Table order_items {
# //   order_id int [ref: > orders.id] // inline relationship (many-to-one)
# //   product_id int
# //   quantity int [default: 1] // default value
# // }

# // Ref: order_items.product_id > products.id

# // Table orders {
# //   id int [pk] // primary key
# //   user_id int [not null, unique]
# //   status varchar
# //   created_at varchar [note: 'When order created'] // add column note
# // }

# //----------------------------------------------//

# //// -- Level 3 
# //// -- Enum, Indexes

# // Enum for 'products' table below
# // Enum products_status {
# //   out_of_stock
# //   in_stock
# //   running_low [note: 'less than 20'] // add column note
# // }

# // // Indexes: You can define a single or multi-column index 
# // Table products {
# //   id int [pk]
# //   name varchar
# //   merchant_id int [not null]
# //   price int
# //   status products_status
# //   created_at datetime [default: `now()`]
  
# //   Indexes {
# //     (merchant_id, status) [name:'product_status']
# //     id [unique]
# //   }
# // }

# // Table merchants {
# //   id int
# //   country_code int
# //   merchant_name varchar
  
# //   "created at" varchar
# //   admin_id int [ref: > U.id]
# //   Indexes {
# //     (id, country_code) [pk]
# //   }
# // }

# // Table merchant_periods {
# //   id int [pk]
# //   merchant_id int
# //   country_code int
# //   start_date datetime
# //   end_date datetime
# // }

# // Ref: products.merchant_id > merchants.id // many-to-one
# // //composite foreign key
# // Ref: merchant_periods.(merchant_id, country_code) > merchants.(id, country_code)


# // Ref: "territoriais"."codigo" < "territoriais"."regiao"
# '''