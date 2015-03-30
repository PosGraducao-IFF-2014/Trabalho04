# -*- coding: utf-8 -*-
import os, json

class DB(dict):
    path = os.path.abspath(os.path.dirname(__file__)) + '/DB.json'

    def __init__(self, *args, **kwargs):
        super(DB, self).__init__(*args, **kwargs)
        self.update(json.load(open(self.path, 'r')))

    def adicionar(self, item):
        item['codigo'] = self._proximo_codigo()
        self[item['codigo']] = item
        json.dump(self, open(self.path, 'w'))

    def procurar(self, match):
        return filter(match, self)

    def reset(self):
        json.dump({}, open(self.path, 'w'))

    def _proximo_codigo(self):
        return sorted(self)[-1]+1 if len(self) else 1


class ContaAReceber(dict):

    def salvar(self):
        if self.eh_valido():
            DB().adicionar(self)
        return self.eh_valido()

    def eh_valido(self):
        return True

    @classmethod
    def buscar_por_codigo(self, codigo):
        return DB().get(str(codigo))
