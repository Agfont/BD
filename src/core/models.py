from django.db import models

# Create your models here.
CHARFIELD_LENGTH = 100

class MilitaryChief(models.Model):
    class Meta:
        db_table = 'military_chiefs'

    # id = primary_key    
    rank = models.CharField(max_length=CHARFIELD_LENGTH)
    division_number = models.IntegerField()
    armed_group = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE, null=False)
    leader = models.ForeignKey('PoliticalLeader', on_delete=models.CASCADE)

class PoliticalLeader(models.Model):
    class Meta:
        db_table = 'politcal_leaders'
        unique_together = (("id", "armed_group"),)
     
    name = models.CharField(max_length=CHARFIELD_LENGTH)
    armed_group = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    support = models.CharField(max_length=CHARFIELD_LENGTH)

class ArmedGroup(models.Model):
    class Meta:
        db_table = 'armed_groups'

    code_id = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=CHARFIELD_LENGTH, null=False, blank=False)
    deads = models.IntegerField()

class Division(models.Model):
    class Meta:
        db_table = 'divisions'
        unique_together = (("id", "armed_group"),)
        
    armed_group = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    deads = models.IntegerField()
    boats = models.IntegerField()
    tanks = models.IntegerField()
    planes = models.IntegerField()
    mens = models.IntegerField()

class Organization(models.Model):
    class Meta:
        db_table = 'organizations'
        
    name = models.CharField(max_length=CHARFIELD_LENGTH)
    sort = models.CharField(max_length=CHARFIELD_LENGTH)
    amount_people = models.IntegerField()
    sort_of_help = models.CharField(max_length=CHARFIELD_LENGTH)
    leader = models.CharField(max_length=CHARFIELD_LENGTH)

class Conflict(models.Model):
    class Meta:
        db_table = 'conflicts'

    #id = amount_people = models.IntegerField()
    name = models.CharField(max_length=CHARFIELD_LENGTH)
    sort = models.CharField(max_length=CHARFIELD_LENGTH)
    wounded = models.IntegerField()
    deads = models.IntegerField()


class Weapon(models.Model):
    class Meta:
        db_table = 'weapons'

    name = models.CharField(max_length=CHARFIELD_LENGTH, primary_key=True)
    indicator = models.IntegerField()

class Dealer(models.Model):
    class Meta: 
        db_table = 'dealers'

    name = models.CharField(max_length=CHARFIELD_LENGTH)

class SupplyWeaponArmedGroupDealer(models.Model):
    class Meta:
        db_table = 'supply_weapons_armed_groups_dealers'

    armed_group = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    weapon = models.ForeignKey('Weapon', on_delete=models.CASCADE)
    dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE)
    weapons_amount = models.IntegerField()

class DialogPoliticalLeaderArmedGroupOrganization(models.Model):
    class Meta:
        db_table = 'dialog_political_leaders_armed_groups_organizations'
        unique_together = (('political_leader', 'armed_group', 'organization'))

    political_leader = models.ForeignKey('PoliticalLeader', on_delete=models.CASCADE)
    armed_group = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

class EnterPart(models.Model):
    class Meta:
        db_table = 'enter_part'
        unique_together = (('armed_group', 'conflict', 'enter_date'))

    armed_group = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    enter_date = models.DateField(auto_now=False)

class ExitPart(models.Model):
    class Meta:
        db_table = 'exit_part'
        unique_together = (('armed_group', 'conflict', 'exit_date'))

    armed_group = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    exit_date = models.DateField(auto_now=False)
    
class EnterMed(models.Model):
    class Meta:
        db_table = 'enter_med'
        unique_together = (('organization', 'conflict', 'enter_date'))

    organization = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    enter_date = models.DateField(auto_now=False)

class ExitMed(models.Model):
    class Meta:
        db_table = 'exit_med'
        unique_together = (('organization', 'conflict', 'exit_date'))

    organization = models.ForeignKey('ArmedGroup', on_delete=models.CASCADE)
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    exit_date = models.DateField(auto_now=False)

class CanSupply(models.Model):
    class Meta:
        db_table = 'can_supply'
        unique_together = (('weapon', 'dealer'))

    weapon = models.ForeignKey('Weapon', on_delete=models.CASCADE)
    dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE)
    amount_weapons = models.IntegerField()

class Religious(models.Model):
    class Meta:
        db_table = 'religious_wars'
        unique_together = (('id', 'conflict'))
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)

class Economic(models.Model):
    class Meta:
        db_table = 'economic_wars'
        unique_together = (('id', 'conflict'))
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)
    
class Region(models.Model):
    class Meta:
        db_table = 'region_wars'
        unique_together = (('id', 'conflict'))
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)

class Country(models.Model):
    class Meta:
        db_table = 'country_wars'
        unique_together = (('id', 'conflict'))
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)

class Etnic(models.Model):
    class Meta:
        db_table = 'etnic_wars'
        unique_together = (('id', 'conflict'))        
    conflict = models.ForeignKey('Conflict', on_delete=models.CASCADE)


class PoliticalLeadersMilitaryChiefs(models.Model):
    class Meta:
        db_table = 'political_leaders_military_chiefs'

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