# -*- coding: utf-8 -*-
import os, json

class DB(list):
    path = os.path.abspath(os.path.dirname(__file__)) + '/DB'

    def __init__(self, *args, **kwargs):
        super(DB, self).__init__(*args, **kwargs)
        self.extend(json.load(open(self.path, 'rb')))

    def adicionar(self, item):
        self.append(item)
        json.dump(self, open(self.path, 'wb'))
        return self

    def procurar(self, match):
        return filter(match, self)

    def reset(self):
        json.dump([], open(self.path, 'wr'))

class ContaAReceber(dict):

    def salvar(self):
        if self.eh_valido():
            DB().adicionar(self)
        return self.eh_valido()

    def eh_valido(self):
        return True
