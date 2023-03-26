import json
import os

from pathlib import Path

from atual_path import local_path

base_path = Path(local_path(), './data')


def escrever_json(dados):
    try:
        json_path = os.path.normpath(os.path.join(base_path, 'pars_list.json'))
        with open(json_path, 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    except Exception as e:
        print(e)


def save_wallet(dados, fiat):
    try:
        name_file = f'{fiat}_list.json'
        json_path = os.path.normpath(os.path.join(base_path, name_file))
        with open(json_path, 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    except Exception as e:
        print(e)


def save_settings(obj):
    try:
        json_path = os.path.normpath(os.path.join(base_path, 'settings.json'))
        with open(json_path, 'w', encoding='utf8') as f:
            json.dump(obj, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    except Exception as e:
        print(e)


def escrever_json_all(dados):
    try:
        json_path = os.path.normpath(os.path.join(base_path, 'all_list.json'))
        with open(json_path, 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    except Exception as e:
        print(e)


def ler_json():
    try:
        json_path = os.path.normpath(os.path.join(base_path, 'pars_list.json'))
        with open(json_path, 'r', encoding='utf8') as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return []


def ler_json_all():
    try:
        json_path = os.path.normpath(os.path.join(base_path, 'all_list.json'))
        with open(json_path, 'r', encoding='utf8') as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return []


def ler_list_wallet(fiat):
    name_file = f'{fiat}_list.json'
    try:
        json_path = os.path.normpath(os.path.join(base_path, name_file))
        with open(json_path, 'r', encoding='utf8') as f:
            return json.load(f)
    except:
        return []


def ler_settings():
    try:
        json_path = os.path.normpath(os.path.join(base_path, 'settings.json'))
        with open(json_path, 'r', encoding='utf8') as f:
            return json.load(f)
    except:
        return {"fiat": "BRL"}


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
