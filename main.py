import pandas as pd
import requests as req
import json
import time


def consulta_cnpj():
    dados = pd.read_excel("lista-cnpj.xlsx", sheet_name='Sheet1')
    df = pd.DataFrame(dados, columns=["CNPJ"])
    trarado = []
    for row in df.itertuples():
        trarado.append('{:014}'.format(row[1]))
    df_trarado = pd.DataFrame(trarado)
    lista = []
    for row in df_trarado.itertuples():
            req = req.get('https://www.receitaws.com.br/v1/cnpj/'+str(row[1]))
            req = json.loads(req.text)
            text = {'Nome'      :   req['nome'],
                    'CNPJ'      :   req['cnpj'].replace('.','').replace('/','').replace('-',''),
                    'Telefone'  :   req['email'],
                    'CEP'       :   req['cep'],
                    'Situação'  :   req['situacao']}
            lista.append(text)
            time.sleep(20)
    planilha = pd.DataFrame(lista)
    planilha.to_excel('CNPJ.xlsx')
    return ''