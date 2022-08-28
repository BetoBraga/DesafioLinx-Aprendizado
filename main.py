import pandas as pd
from datetime import date

# Leitura dos dados
offline_sales = pd.read_json("offline_sales.json.gz", lines=True,compression='gzip')
online_orders = pd.read_json("online_orders.json.gz", lines=True,compression='gzip')
online_pageviews = pd.read_json("online_pageviews.json.gz", lines=True,compression='gzip')

# Soma da Coluna
total_sales_offline = float(offline_sales['price'].sum())
total_sales_offline_formatado = format(total_sales_offline, ".2f")

# Soma da Coluna
total_online_orders = float(online_orders['price'].sum())
total_online_orders_formatado = format(total_online_orders, ".2f")

print(f'Faturamento de Vendas Offline: R${total_sales_offline_formatado}')
print(f'Faturamento de Vendas Online: R${total_online_orders_formatado}')

total_ = total_online_orders_formatado + total_sales_offline_formatado
total_ = format(total_, ".2f")
print(f'Faturamento Total de Vendas: R${total_}')

# Produto mais vendido
mais_vendido_on = online_orders.groupby(['on_product_id']).sum().sort_values("quantity", ascending=False)
print('O ID do Produto mais vendido online no período é', mais_vendido_on.index[0])

mais_vendido_off = offline_sales.groupby(['off_product_id']).sum().sort_values("quantity", ascending=False)
print('O ID do Produto mais vendido online no período é', mais_vendido_off.index[0])


# Declaração de Final de Semana
fimdesemana = semana = d = 0
data = pd.to_datetime(offline_sales['date'],errors='ignore') 


while d < len(data)-1:
    carioca = offline_sales['state'][d]
    if carioca == "RJ": 
        data_ = data[d]
        resultado = len(pd.bdate_range(data_,data_))
        if resultado == 0 :
            fimdesemana += 1
        else:
            semana += 1 
    d += 1

if semana > fimdesemana:
    resposta_q3 = 'preferem'
else:
    resposta_q3 = 'não preferem'
    
print(f'Os cariocas {resposta_q3} fazer compras aos fins de semana. ')

# Declaração de costumers
preferiu = nao_preferiu = 0
lista_offline_customer_id = offline_sales['customer_id'].tolist()

for i in online_pageviews['customer_id']:
    if online_pageviews['customer_id'][i] in lista_offline_customer_id:
        preferiu += 1
    else:
        nao_preferiu += 1

if preferiu > nao_preferiu:
    resposta_q4 = 'comprar na loja física'
else:
    resposta_q4 = 'não comprar na loja física'
    
print(f'É da preferência dos clientes {resposta_q4}')

# Declaração de costumers que nao compraram mas acessaram a página
comprou = nao_comprou = 0
lista_online_customer_id_pageviews = online_pageviews['customer_id'].tolist()


for i in online_orders['customer_id']:
    if online_orders['customer_id'][i] in lista_online_customer_id_pageviews:
        comprou += 1
    else:
        nao_comprou += 1

numero_clientes = online_orders.groupby('customer_id')

faturamento_promo = (nao_comprou * total_online_orders_formatado) / numero_clientes.ngroups 
faturamento_com_desc = faturamento_promo - (faturamento_promo * 0.20)
faturamento = format(faturamento_com_desc, ".2f")
print(f'Os efeitos da promoção irão gerar um faturamento de R${faturamento_com_desc}')



