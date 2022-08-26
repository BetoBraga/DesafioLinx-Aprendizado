# O Desafio
Disponibilizamos uma amostra de vendas e visitas anonimizadas de uma rede que tem várias lojas físicas e também uma loja virtual.

Sua tarefa é entender essa base de dados e nos mostrar insights que ajudem esse varejista a
entender como melhorar sua operação.

Para chegar lá você terá que:

- Baixar e carregar os dados no seu computador;

- Interpretar o questionário e entender o que está sendo pedido;

- Escrever código legível, reproduzível e eficiente para calcular as métricas;

- Apresentar os resultados com as tabelas e gráficos apropriados.

## Insumos

São fornecidos três tipos de dados: vendas de loja física, páginas visitadas do ecommerce e
pedidos feitos no ecommerce.

Todas as informações potencialmente sensíveis foram anonimizadas. A identificação do
consumidor customer_id é a mesma tanto no online como offline, porém o catálogo de
produtos não (off_product_id é diferente de on_product_id).

Offline Sales
https://ml-challenge.s3.amazonaws.com/ds-intern-2020/offline_sales.json.gz

Itens de vendas de loja física. Itens comprados na mesma venda terão o mesmo sale_id.
```
{
"date": "2018-08-01",
"state": "RN",
"store_id": "3162633",
"sale_id": "666639323036376",
"off_product_id": "643839313363376",
"quantity": 1,
"price": 149.0,
"customer_id": "30373934343338363136"
}
```
Online Pageviews
https://ml-challenge.s3.amazonaws.com/ds-intern-2020/online_pageviews.json.gz

Páginas visitadas no ecommerce.
```
{
"date": "2018-08-01",
"visitor_id": "3832636531373538373137373",
"deviceType": "mobile",
"pageType": "product",
"category_id": "6365313034",
"on_product_id": "323239323839626",
"customer_id": "33343163316564313264"
}
```
Online Orders
https://ml-challenge.s3.amazonaws.com/ds-intern-2020/online_orders.json.gz

Itens de venda no ecommerce. Itens comprados no mesmo pedido terão o mesmo sale_id.
```
{
"date": "2018-08-01",
"visitor_id": "3430316531623964316332613",
"deviceType": "mobile",
"order_id": "356664366366353",
"on_product_id": "313562333039323",
"quantity": 1,
"price": 629.0,
"customer_id": "63393337303931353431"
}
```
## Perguntas

Usando esses dados, responda às perguntas a seguir.

Você irá notar que as perguntas vão ficando cada vez mais amplas e ambíguas. Você terá que
tomar decisões de interpretação e metodologia, registrando sempre as suposições e
simplificações assumidas.

Lembre-se sempre que utilidade e interpretabilidade são as características mais importantes de
uma boa métrica.

Ressaltamos também que preferimos respostas caprichadas de menos perguntas do que
respostas incompletas de todas as perguntas. Se acabar o prazo, mande o que tem.

1. Qual foi o faturamento total no período?
2. Qual o produto mais comprado online?
3. Cariocas gostam de comprar no fim de semana?
4. É comum escolher online e terminar a compra na loja física?
5. O time de marketing desta rede quer fazer uma campanha oferecendo
um cupom de 20% nas compras de loja física para quem visitou o site e
abandonou um carrinho com produtos. Estime o resultado dessa
campanha.
