from datetime import datetime

import requests

from sqlite_data import select_all, select_wallet, update_my_wallet, update_all_list

prices = []


def consult_price(pesq):
    val = par(prices, pesq)
    try:
        cor = '#55ff00' if float(val[1]) > 0 else '#ff5500'
        prt = f'{val[0]}', f'{float(val[2]):.3f}', f'{float(val[1]):.2f}', cor
    except Exception as e:
        print(e)
        prt = f'{val[0]}', '0.000', '0.00', '#FFF'
    return prt


def cotacao():
    link = 'https://api2.binance.com/api/v3/ticker/24hr'
    req = requests.get(link)
    res = req.json()
    global prices
    prices = res
    return res


def par(res, p):
    if res == 0:
        res = prices
    for coin in res:
        if coin['symbol'] == p:
            return p, coin['priceChangePercent'], coin['bidPrice']


def consulta():
    ret = cotacao()
    pares = select_all('par_list')
    li = list()
    for p in pares:
        val = par(ret, p)
        prt = f'{val[0]}', f'{float(val[2]):.3f}', f'{float(val[1]):.2f}'
        li.append(prt)
    return li


def update_wallet(fiat):
    li_par = []
    li_mon = select_wallet(fiat)
    for item in li_mon:
        val = par(prices, item['par'])
        sub = float(val[2]) * float(item['quant'])
        up = [str(item['par']),  f"{float(val[2]):.6f}", str(item['quant']),  f'{float(sub):.2f}']
        li_par.append(up)
    update_my_wallet(li_par, fiat)
    return li_par


def lista_nova():
    list_new = []
    despised = 0
    for item in prices:
        if float(item['priceChangePercent']) == 0.0:
            despised += 1
        else:
            list_new.append(item['symbol'])
    update_all_list(list_new)
    return despised


def data_e_hora():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
    return data_e_hora_em_texto
