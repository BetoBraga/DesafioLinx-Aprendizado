import pandas as pd
from datetime import date

# Leitura dos dados
offline_sales = pd.read_json("offline_sales.json.gz", lines=True,compression='gzip')
online_orders = pd.read_json("online_orders.json.gz", lines=True,compression='gzip')

# Soma da Coluna
total_sales_offline = float(offline_sales['price'].sum())
total_sales_offline_formatado = format(total_sales_offline, ".2f")

# Soma da Coluna
total_online_orders = float(online_orders['price'].sum())
total_online_orders_formatado = format(total_online_orders, ".2f")

print(f'Faturamento de Vendas Offline: R${total_sales_offline_formatado}')
print(f'Faturamento de Vendas Online: R${total_online_orders_formatado}')

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

# REALIZAR 4 E 5 QUESTÕES
