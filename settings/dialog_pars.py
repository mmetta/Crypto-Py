import json
import os


app_path = os.path.abspath(os.getcwd())
folder = "settings"
path = os.path.join(app_path, folder)


def escrever_json(dados):
    json_path = os.path.normpath(os.path.join(path, 'pars_list.json'))
    with open(json_path, 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))


def escrever_json_all(dados):
    json_path = os.path.normpath(os.path.join(path, 'all_list.json'))
    with open(json_path, 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))


def ler_json():
    json_path = os.path.normpath(os.path.join(path, 'pars_list.json'))
    with open(json_path, 'r', encoding='utf8') as f:
        return json.load(f)


def ler_json_all():
    json_path = os.path.normpath(os.path.join(path, 'all_list.json'))
    with open(json_path, 'r', encoding='utf8') as f:
        return json.load(f)


def alterar_json(upd, i):
    pares = ler_json()
    pares[i] = upd
    escrever_json(pares)


def delete_json(index):
    pares = ler_json()
    lista = []
    for i, par in enumerate(pares):
        if i != index:
            lista.append(par)
        escrever_json(lista)


def inserir_json(par):
    pares = list(ler_json())
    pares.append(par)
    escrever_json(pares)
