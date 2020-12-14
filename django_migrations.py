BEGIN;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
--                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
-- Create model ArmedGroup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
--                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
CREATE TABLE "armed_groups" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "deads" integer NOT NULL);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
--                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
-- Create model Conflict                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
--                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
CREATE TABLE "conflicts" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "sort" varchar(100) NOT NULL, "wounded" integer NOT NULL, "deads" integer NOT NULL);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
--                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
-- Create model Dealer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
--                                                                                                                                                                                                                                                                                                                              
CREATE TABLE "dealers" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL);                                                                                                                                                                                                                                        
--                                                                                                                                                                                                                                                                                                                              
-- Create model MilitaryChief                                                                                                                                                                                                                                                                                                   
--                                                                                                                                                                                                                                                                                                                              
CREATE TABLE "military_chiefs" ("id" serial NOT NULL PRIMARY KEY, "rank" varchar(100) NOT NULL, "division_number" integer NOT NULL, "armed_group_id" integer NOT NULL);                                              
--                                                                                                        
-- Create model Organization                                                                              
--                                                                                                                                                                                                                   
CREATE TABLE "organizations" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "sort" varchar(100) NOT NULL, "amount_people" integer NOT NULL, "sort_of_help" varchar(100) NOT NULL, "leader" varchar(100) NOT NULL);                                                                                                                                                                                                      
--                                                                                                        
-- Create model PoliticalLeader                                                                           
--                                                                                                                                                                                                                   
CREATE TABLE "politcal_leaders" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "support" varchar(100) NOT NULL, "armed_group_id" integer NOT NULL);                                                
--                                                                                                        
-- Create model Weapon                                                                                    
--                                                                                                        
CREATE TABLE "weapons" ("name" varchar(100) NOT NULL PRIMARY KEY, "indicator" integer NOT NULL);                                                                                                                     
--                                                                                                        
-- Create model SupplyWeaponArmedGroupDealer                                                              
--                                                                                                        
CREATE TABLE "supply_weapons_armed_groups_dealers" ("id" serial NOT NULL PRIMARY KEY, "weapons_amount" integer NOT NULL, "armed_group_id" integer NOT NULL, "dealer_id" integer NOT NULL, "weapon_id" varchar(100) NOT NULL);                                                                                                                                                                                                             
--                                                                                                        
-- Create model PoliticalLeadersMilitaryChiefs                                                            
--                                                                                                        
CREATE TABLE "political_leaders_military_chiefs" ("id" serial NOT NULL PRIMARY KEY, "military_chief_id" integer NOT NULL, "political_leader_id" integer NOT NULL);                                                   
--                                                                                                        
-- Add field leader to militarychief                                                                      
--                                                                                                        
ALTER TABLE "military_chiefs" ADD COLUMN "leader_id" integer NOT NULL CONSTRAINT "military_chiefs_leader_id_fcd46e8e_fk_politcal_leaders_id" REFERENCES "politcal_leaders"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "military_chiefs_leader_id_fcd46e8e_fk_politcal_leaders_id" IMMEDIATE;                                                                                                                                    
--                                                                                                        
-- Create model Religious                                                                                 
--                                                                                                        
CREATE TABLE "religious_wars" ("id" serial NOT NULL PRIMARY KEY, "conflict_id" integer NOT NULL);                                                                                                                    
--                                                                                                        
-- Create model Region                                                                                    
--                                                                                                        
CREATE TABLE "region_wars" ("id" serial NOT NULL PRIMARY KEY, "conflict_id" integer NOT NULL);                                                                                                                       
--                                                                                                        
-- Create model ExitPart                                                                                  
--                                                                                                        
CREATE TABLE "exit_part" ("id" serial NOT NULL PRIMARY KEY, "exit_date" date NOT NULL, "armed_group_id" integer NOT NULL, "conflict_id" integer NOT NULL);                                                           
--                                                                                                        
-- Create model ExitMed                                                                                   
--                                                                                                                                                              
CREATE TABLE "exit_med" ("id" serial NOT NULL PRIMARY KEY, "exit_date" date NOT NULL, "conflict_id" integer NOT NULL, "organization_id" integer NOT NULL);                                                                                                                                                                      
--                                                                                                                                                              
-- Create model Etnic                                                                                                                                           
--                                                                                                                                                              
CREATE TABLE "etnic_wars" ("id" serial NOT NULL PRIMARY KEY, "conflict_id" integer NOT NULL);                                                                   
--                                                                                                                                                              
-- Create model EnterPart                                                                                                                                       
--                                                                                                                                                              
CREATE TABLE "enter_part" ("id" serial NOT NULL PRIMARY KEY, "enter_date" date NOT NULL, "armed_group_id" integer NOT NULL, "conflict_id" integer NOT NULL);                                                                                                                                                                    
--                                                                                                                                                              
-- Create model EnterMed                                                                                                                                        
--                                                                                                                                                              
CREATE TABLE "enter_med" ("id" serial NOT NULL PRIMARY KEY, "enter_date" date NOT NULL, "conflict_id" integer NOT NULL, "organization_id" integer NOT NULL);                                                                                                                                                                    
--                                                                                                                                                              
-- Create model Economic                                                                                                                                        
--                                                                                                                                                              
CREATE TABLE "economic_wars" ("id" serial NOT NULL PRIMARY KEY, "conflict_id" integer NOT NULL);                                                                
--                                                                                                                                                              
-- Create model Division                                                                                                                                        
--                                                                                                                                                              
CREATE TABLE "divisions" ("id" serial NOT NULL PRIMARY KEY, "deads" integer NOT NULL, "boats" integer NOT NULL, "tanks" integer NOT NULL, "planes" integer NOT NULL, "mens" integer NOT NULL, "armed_group_id" integer NOT NULL);                                                                                               
--                                                                                                                                                              
-- Create model DialogPoliticalLeaderArmedGroupOrganization                                                                                                     
--                                                                                                                                                              
CREATE TABLE "dialog_political_leaders_armed_groups_organizations" ("id" serial NOT NULL PRIMARY KEY, "armed_group_id" integer NOT NULL, "organization_id" integer NOT NULL, "political_leader_id" integer NOT NULL);                                                                                                           
--                                                                                                                                                              
-- Create model Country                                                                                                                                         
--                                                                                                                                                              
CREATE TABLE "country_wars" ("id" serial NOT NULL PRIMARY KEY, "conflict_id" integer NOT NULL);                                                                 
--                                                                                                                                                              
-- Create model CanSupply                                                                                                                                       
--                                                                                                                              

CREATE TABLE "can_supply" ("id" serial NOT NULL PRIMARY KEY, "amount_weapons" integer NOT NULL, "dealer_id" integer NOT NULL, "weapon_id" varchar(100) NOT NULL);
ALTER TABLE "military_chiefs" ADD CONSTRAINT "military_chiefs_armed_group_id_1d8fb18d_fk_armed_groups_id" FOREIGN KEY ("armed_group_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "military_chiefs_armed_group_id_1d8fb18d" ON "military_chiefs" ("armed_group_id");
ALTER TABLE "politcal_leaders" ADD CONSTRAINT "politcal_leaders_id_armed_group_id_71d8289e_uniq" UNIQUE ("id", "armed_group_id");
ALTER TABLE "politcal_leaders" ADD CONSTRAINT "politcal_leaders_armed_group_id_f5664065_fk_armed_groups_id" FOREIGN KEY ("armed_group_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "politcal_leaders_armed_group_id_f5664065" ON "politcal_leaders" ("armed_group_id");
CREATE INDEX "weapons_name_e5088bd0_like" ON "weapons" ("name" varchar_pattern_ops);
ALTER TABLE "supply_weapons_armed_groups_dealers" ADD CONSTRAINT "supply_weapons_armed_armed_group_id_b37410f6_fk_armed_gro" FOREIGN KEY ("armed_group_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "supply_weapons_armed_groups_dealers" ADD CONSTRAINT "supply_weapons_armed_dealer_id_c436fa56_fk_dealers_i" FOREIGN KEY ("dealer_id") REFERENCES "dealers" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "supply_weapons_armed_groups_dealers" ADD CONSTRAINT "supply_weapons_armed_weapon_id_6700ccc2_fk_weapons_n" FOREIGN KEY ("weapon_id") REFERENCES "weapons" ("name") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "supply_weapons_armed_groups_dealers_armed_group_id_b37410f6" ON "supply_weapons_armed_groups_dealers" ("armed_group_id");
CREATE INDEX "supply_weapons_armed_groups_dealers_dealer_id_c436fa56" ON "supply_weapons_armed_groups_dealers" ("dealer_id");
CREATE INDEX "supply_weapons_armed_groups_dealers_weapon_id_6700ccc2" ON "supply_weapons_armed_groups_dealers" ("weapon_id");
CREATE INDEX "supply_weapons_armed_groups_dealers_weapon_id_6700ccc2_like" ON "supply_weapons_armed_groups_dealers" ("weapon_id" varchar_pattern_ops);
ALTER TABLE "political_leaders_military_chiefs" ADD CONSTRAINT "political_leaders_mi_military_chief_id_9dc6fddb_fk_military_" FOREIGN KEY ("military_chief_id") REFERENCES "military_chiefs" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "political_leaders_military_chiefs" ADD CONSTRAINT "political_leaders_mi_political_leader_id_83bc774c_fk_politcal_" FOREIGN KEY ("political_leader_id") REFERENCES "politcal_leaders" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "political_leaders_military_chiefs_military_chief_id_9dc6fddb" ON "political_leaders_military_chiefs" ("military_chief_id");
CREATE INDEX "political_leaders_military_chiefs_political_leader_id_83bc774c" ON "political_leaders_military_chiefs" ("political_leader_id");
CREATE INDEX "military_chiefs_leader_id_fcd46e8e" ON "military_chiefs" ("leader_id");
ALTER TABLE "religious_wars" ADD CONSTRAINT "religious_wars_id_conflict_id_2c953a1f_uniq" UNIQUE ("id", "conflict_id");
ALTER TABLE "religious_wars" ADD CONSTRAINT "religious_wars_conflict_id_632f0c59_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "religious_wars_conflict_id_632f0c59" ON "religious_wars" ("conflict_id");
ALTER TABLE "region_wars" ADD CONSTRAINT "region_wars_id_conflict_id_6ea4a721_uniq" UNIQUE ("id", "conflict_id");
ALTER TABLE "region_wars" ADD CONSTRAINT "region_wars_conflict_id_cd8d70a2_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "region_wars_conflict_id_cd8d70a2" ON "region_wars" ("conflict_id");
ALTER TABLE "exit_part" ADD CONSTRAINT "exit_part_armed_group_id_conflict_id_exit_date_8cc7a30c_uniq" UNIQUE ("armed_group_id", "conflict_id", "exit_date");
ALTER TABLE "exit_part" ADD CONSTRAINT "exit_part_armed_group_id_fe6e2e11_fk_armed_groups_id" FOREIGN KEY ("armed_group_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "exit_part" ADD CONSTRAINT "exit_part_conflict_id_53038b44_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "exit_part_armed_group_id_fe6e2e11" ON "exit_part" ("armed_group_id");
CREATE INDEX "exit_part_conflict_id_53038b44" ON "exit_part" ("conflict_id");
ALTER TABLE "exit_med" ADD CONSTRAINT "exit_med_organization_id_conflict_id_exit_date_9c26e353_uniq" UNIQUE ("organization_id", "conflict_id", "exit_date");
ALTER TABLE "exit_med" ADD CONSTRAINT "exit_med_conflict_id_6c7a8751_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "exit_med" ADD CONSTRAINT "exit_med_organization_id_5de7ed28_fk_armed_groups_id" FOREIGN KEY ("organization_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "exit_med_conflict_id_6c7a8751" ON "exit_med" ("conflict_id");
CREATE INDEX "exit_med_organization_id_5de7ed28" ON "exit_med" ("organization_id");
ALTER TABLE "etnic_wars" ADD CONSTRAINT "etnic_wars_id_conflict_id_4f2e9474_uniq" UNIQUE ("id", "conflict_id");
ALTER TABLE "etnic_wars" ADD CONSTRAINT "etnic_wars_conflict_id_8ca08d72_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "etnic_wars_conflict_id_8ca08d72" ON "etnic_wars" ("conflict_id");
ALTER TABLE "enter_part" ADD CONSTRAINT "enter_part_armed_group_id_conflict_id_enter_date_96de999e_uniq" UNIQUE ("armed_group_id", "conflict_id", "enter_date");
ALTER TABLE "enter_part" ADD CONSTRAINT "enter_part_armed_group_id_919fe368_fk_armed_groups_id" FOREIGN KEY ("armed_group_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "enter_part" ADD CONSTRAINT "enter_part_conflict_id_b8f3246d_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "enter_part_armed_group_id_919fe368" ON "enter_part" ("armed_group_id");
CREATE INDEX "enter_part_conflict_id_b8f3246d" ON "enter_part" ("conflict_id");
ALTER TABLE "enter_med" ADD CONSTRAINT "enter_med_organization_id_conflict_id_enter_date_f5ad422b_uniq" UNIQUE ("organization_id", "conflict_id", "enter_date");
ALTER TABLE "enter_med" ADD CONSTRAINT "enter_med_conflict_id_f9775079_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "enter_med" ADD CONSTRAINT "enter_med_organization_id_df4ae56d_fk_armed_groups_id" FOREIGN KEY ("organization_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "enter_med_conflict_id_f9775079" ON "enter_med" ("conflict_id");
CREATE INDEX "enter_med_organization_id_df4ae56d" ON "enter_med" ("organization_id");
ALTER TABLE "economic_wars" ADD CONSTRAINT "economic_wars_id_conflict_id_aa34a8cc_uniq" UNIQUE ("id", "conflict_id");
ALTER TABLE "economic_wars" ADD CONSTRAINT "economic_wars_conflict_id_1d6a50fc_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "economic_wars_conflict_id_1d6a50fc" ON "economic_wars" ("conflict_id");
ALTER TABLE "divisions" ADD CONSTRAINT "divisions_id_armed_group_id_0dffa4b2_uniq" UNIQUE ("id", "armed_group_id");
ALTER TABLE "divisions" ADD CONSTRAINT "divisions_armed_group_id_8ec6145e_fk_armed_groups_id" FOREIGN KEY ("armed_group_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "divisions_armed_group_id_8ec6145e" ON "divisions" ("armed_group_id");
ALTER TABLE "dialog_political_leaders_armed_groups_organizations" ADD CONSTRAINT "dialog_political_leaders_political_leader_id_arme_9c6ec2ae_uniq" UNIQUE ("political_leader_id", "armed_group_id", "organization_id");
ALTER TABLE "dialog_political_leaders_armed_groups_organizations" ADD CONSTRAINT "dialog_political_lea_armed_group_id_61ebd1a8_fk_armed_gro" FOREIGN KEY ("armed_group_id") REFERENCES "armed_groups" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "dialog_political_leaders_armed_groups_organizations" ADD CONSTRAINT "dialog_political_lea_organization_id_cd96e639_fk_organizat" FOREIGN KEY ("organization_id") REFERENCES "organizations" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "dialog_political_leaders_armed_groups_organizations" ADD CONSTRAINT "dialog_political_lea_political_leader_id_e6ba0318_fk_politcal_" FOREIGN KEY ("political_leader_id") REFERENCES "politcal_leaders" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "dialog_political_leaders_a_armed_group_id_61ebd1a8" ON "dialog_political_leaders_armed_groups_organizations" ("armed_group_id");
CREATE INDEX "dialog_political_leaders_a_organization_id_cd96e639" ON "dialog_political_leaders_armed_groups_organizations" ("organization_id");
CREATE INDEX "dialog_political_leaders_a_political_leader_id_e6ba0318" ON "dialog_political_leaders_armed_groups_organizations" ("political_leader_id");
ALTER TABLE "country_wars" ADD CONSTRAINT "country_wars_id_conflict_id_29bcf858_uniq" UNIQUE ("id", "conflict_id");
ALTER TABLE "country_wars" ADD CONSTRAINT "country_wars_conflict_id_349400b8_fk_conflicts_id" FOREIGN KEY ("conflict_id") REFERENCES "conflicts" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "country_wars_conflict_id_349400b8" ON "country_wars" ("conflict_id");
ALTER TABLE "can_supply" ADD CONSTRAINT "can_supply_weapon_id_dealer_id_b03d3fc4_uniq" UNIQUE ("weapon_id", "dealer_id");
ALTER TABLE "can_supply" ADD CONSTRAINT "can_supply_dealer_id_a7f08c74_fk_dealers_id" FOREIGN KEY ("dealer_id") REFERENCES "dealers" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "can_supply" ADD CONSTRAINT "can_supply_weapon_id_5e216f7a_fk_weapons_name" FOREIGN KEY ("weapon_id") REFERENCES "weapons" ("name") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "can_supply_dealer_id_a7f08c74" ON "can_supply" ("dealer_id");
CREATE INDEX "can_supply_weapon_id_5e216f7a" ON "can_supply" ("weapon_id");
CREATE INDEX "can_supply_weapon_id_5e216f7a_like" ON "can_supply" ("weapon_id" varchar_pattern_ops);
COMMIT;
