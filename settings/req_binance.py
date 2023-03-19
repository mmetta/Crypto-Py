from datetime import datetime

import requests

from settings.dialog_pars import ler_json, escrever_json_all

prices = []


def consult_price(pesq):
    val = par(prices, pesq)
    try:
        if float(val[1]) > 0:
            cor = '#00FF00'
        else:
            cor = '#FF0000'
        prt = f'{val[0]}', f'{float(val[2]):.3f}', f'{float(val[1]):.2f}', cor
    except Exception as e:
        print(e)
        prt = f'{val[0]}', '0.000', '0.00', '#FFF'
    return prt


def lista_nova():
    list_new = []
    despised = 0
    for item in prices:
        if float(item['priceChangePercent']) == 0.0:
            despised += 1
        else:
            list_new.append(item['symbol'])
    escrever_json_all(list_new)
    return despised


def cotacao():
    link = 'https://api2.binance.com/api/v3/ticker/24hr'
    req = requests.get(link)
    res = req.json()
    global prices
    prices = res
    return res


def par(res, p):
    for coin in res:
        if coin['symbol'] == p:
            return p, coin['priceChangePercent'], coin['bidPrice']


def consulta():
    ret = cotacao()
    pares = ler_json()
    li = list()
    for p in pares:
        val = par(ret, p)
        prt = f'{val[0]}', f'{float(val[2]):.3f}', f'{float(val[1]):.2f}'
        li.append(prt)
    return li


def fc(v):
    if float(v) >= 0:
        c = 'SUCCESS'
    else:
        c = 'DANGER'
    return c


def data_e_hora():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
    return data_e_hora_em_texto
