
# Exercicio 2.a

## Permita cadastrar divisões dentro de um grupo militar, cadastre conflitos bélicos, grupos militares, líderes políticos e chefes militares

1- divisoes

endpoint:
POST /v1/divisions

payload de envio
```javascript
{
  "group_code": int,
  "casualities": int,
  "boats": int,
  "tanks": int,
  "planes": int,
  "men": int 
}
```
retorno é o mesmo, com um campo id

2- grupos armados / grupo militar?

endpoint:
POST /v1/armed-groups

payload de envio:
```javascript
{
  "name": string,
  "casualities": int
  "division": {
    "group_code": int,
    "casualities": int,
    "boats": int,
    "tanks": int,
    "planes": int,
    "men": int 
  }
}
```
retorno é o mesmo, com um campo id nos 2 níveis! (no mesmo nivel de name e dentro do objeto division)

3 - conflitos

endpoint:
POST /v1/conflicts

payload de envio
```javascript
{
  "name": string,
  "sort": string,
  "wounded": int,
  "casualties": int,
  "sort": string
}
```
retorno é o mesmo, com um campo id

4 - lideres politicos

endpoint:
POST /v1/political-leaders

payload de envio
```javascript
{
  "group_id": int,
  "name": string,
  "support": string
 }
```
retorno é o mesmo, com um campo id


5 - chefe militar

endpoint:
POST /v1/military-chiefs

payload de envio
```javascript
 {
  "sash": string, 
  "division_id": int,
  "group_id": int
}
```

retorno é o mesmo, com um campo id

# 2.b

## i) Gerar um gráfico, histograma, por tipo de conflito e número de conflitos.

endpoint:
GET /v1/conflicts/graphs/sort

payload de envio : NADA

example return payload for /sort
```javascript
{
  "data": [
    "sort1": [
      {
        "id": int,
        "name": string,
        "sort": string,
        "wounded": int,
        "casualties": int,
        "sort": "sort1"
      },
      {
        "id": int,
        "name": string,
        "sort": string,
        "wounded": int,
        "casualties": int,
        "sort": "sort1"
      },
    ],
    "sort2": [
      {
        "id": int,
        "name": string,
        "sort": string,
        "wounded": int,
        "casualties": int,
        "sort": "sort2"
      },
      {
        "id": int,
        "name": string,
        "sort": string,
        "wounded": int,
        "casualties": int,
        "sort": "sort2"
      }
    ],
    [...]
  ]
}
```
endpoint:
GET /v1/conflicts/graphs/{conflict_id}
example return payload for /10  

payload de envio: NADA
```javascript
{
  "id": 10,
  "name": string,
  "sort": string,
  "wounded": int,
  "casualties": int,
  "sort": "sort2"
}
```

## ii) Listar os traficantes e os grupos armados (Nome) para os quais os traficantes fornecem armas “Barret M82” ou “M200 intervention”.

<!-- esse endpoint está um lixo, opniões melhores são bem vindas -->
endpoint:
GET /v1/dealers/barret-m82-or-m200-intervention

payload de envio: NADA

retorno
```javascript
{
  "data": [
    {
      "name": string,
      "gun":{
        "name": string,
        "indicator": int
      }
    },
    {
      "name": string,
      "gun":{
        "name": string,
        "indicator": int
      }
    },
    [...]
  ]
}
```

## iii) Listar os 5 maiores conflitos em número de mortos.

endpoint: /v1/top5/conflicts
payload de envio: NADA
retorno
```javascript
{
  "data": [
    {
      conflict1,
    },
    {
      conflict2
    },
    ...
  ]
}
```

## iv.Listar as 5 maiores organizações em número de mediações.

endpoint: /v1/top5/organizations
payload de envio: NADA
retorno
```javascript
{
  "data": [
    {
      organization1,
    },
    {
      organization2,
    },
    ...
  ]
}
```

## v.Listar os 5 maiores grupos armados com maior número de armas fornecidos.

endpoint: /v1/top5/armed-group
payload de envio: NADA
retorno
```javascript
{
  "data": [
    {
      armed_group1
    },
    {
      armed_group2
    },
    ...
  ]
}

```

## vi.Listar o país e número de conflitos com maior número de conflitos religiosos
endpoint: /v1/religious-conflict
payload de envio: NADA
retorno
```javascript
{
  "data": [
    {
      "country": string,
      "conflicts_amount": int
    },
    {
      "country": string,
      "conflicts_amount": int
    },
  ]
}
```

{
  "comment": "chefes_lider",
  "method" : "POST",
  "codigo_chef": 0,
  "codigo_lider": 0
}

{
  "comment": "ConfRelig",
  "method" : "GET",
  "conflito_id": 0,
  "religiao": "religiao"
}
{
  "comment": "ConfEcon",
  "method" : "GET",
  "conflito_id": 0,
  "mat_prima": "mat_prima"
}
{
  "comment": "ConfRegiao",
  "method" : "GET",
  "conflito_id": 0,
  "religiao": "regiao"
}
{
  "comment": "ConfPais",
  "method" : "GET",
  "conflito_id": 0,
  "religiao": "pais"
}
{
  "comment": "ConfEtnia",
  "method" : "GET",
  "conflito_id": 0,
  "religiao": "etnia"
}

{
  "comment": "traficantes",
  "method" : "GET",
  "conflito_id": 0,
  "arma": [
  	{
  	"a" : "Barret M82",
  	"b" : "M200 intervention"
  	}
 ]
}
