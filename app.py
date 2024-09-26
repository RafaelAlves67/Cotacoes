import requests
import pandas as pd 
from datetime import datetime 
import time 

while True:
    # Requisição à API
    req = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    req_dic = req.json() 

    # Acessando as cotações corretamente
    cotacao_dolar = req_dic["USDBRL"]["bid"] 
    cotacao_euro = req_dic["EURBRL"]["bid"]
    cotacao_btc = req_dic["BTCBRL"]["bid"]

    # Leitura da planilha que vai ser alimentada
    df_cotacao = pd.read_excel('Cotações.xlsx')  

    # Atualizando a planilha com as cotações
    df_cotacao.loc[0, "Cotação"] = float(cotacao_dolar) 
    df_cotacao.loc[1, "Cotação"] = float(cotacao_euro)
    df_cotacao.loc[2, "Cotação"] = float(cotacao_btc) * 1000  # Multiplicando BTC por 1000 como no seu código

    # Atualizando a data da última atualização
    df_cotacao.loc[0, "Data Última Atualização"] = datetime.now() 

    # Salvando a planilha atualizada
    df_cotacao.to_excel("Cotações.xlsx", index=False)

    # Mensagem de confirmação
    print(f"Cotação concluída. {datetime.now()}")

    # Espera de 60 segundos antes da próxima iteração
    time.sleep(60)
