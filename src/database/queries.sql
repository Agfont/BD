
-- i
select tipo, count(distinct codigo) as quantidade
from conflitos
group by tipo
order by tipo asc

-- ii
SELECT traficantes.nome_traficante as traficante, grupos_armados.nome_grupo as grupo, nome_arma as arma
FROM fornece 
JOIN traficantes ON fornece.id_traficante = traficantes.id_traficante
JOIN grupos_armados ON fornece.codigo_grupo = grupos_armados.id
WHERE nome_arma = 'Barret M82' OR nome_arma = 'M200 intervention';

-- iii
select * 
from conflitos 
order by num_mortos desc 
limit 5;

-- iv
SELECT nome_org, COUNT(*) as num_intermed
FROM organizacoes_m
JOIN "EntraMed" ON organizacoes_m.codigo_org = "EntraMed".codigo_org
GROUP BY "EntraMed".codigo_org, organizacoes_m.codigo_org
ORDER BY num_intermed 
DESC LIMIT 5;



-- v
SELECT grupos_armados.nome_grupo, SUM(num_armas) as total
FROM fornece
join grupos_armados on fornece.codigo_grupo = grupos_armados.id
GROUP BY grupos_armados.nome_grupo
ORDER BY total DESC LIMIT 5;


-- vi
SELECT regiao, COUNT(conflito_id) as conflitos
FROM "ConfRegiao"
GROUP BY regiao
ORDER BY conflitos 
DESC limit 1;