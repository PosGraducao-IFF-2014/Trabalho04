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
        self.salvar_em_disco()

    def remover(self, codigo):
        if self.has_key(codigo):
            self.pop(codigo)
            self.salvar_em_disco()

    def procurar(self, match):
        return filter(match, self)

    def reset(self):
        self.clear()
        self.salvar_em_disco()

    def salvar_em_disco(self):
        json.dump(self, open(self.path, 'w'))

    def _proximo_codigo(self):
        return int(sorted(self)[-1])+1 if len(self) else 1


class ContaAReceber(dict):

    def salvar(self):
        if self.eh_valido():
            DB().adicionar(self)
        return self.eh_valido()

    def eh_valido(self):
        return True

    def remover(self):
        DB().remover(str(self['codigo']))

    @classmethod
    def buscar(cls, codigo):
        resultado = DB().get(str(codigo))
        return resultado and cls(resultado)

    @classmethod
    def todas(cls):
        return map(lambda r: cls(r), DB().values())
