# -*- coding: utf-8 -*-
import json, requests, time, unittest, os
from subprocess import Popen
from models import DB

class ServerTest(unittest.TestCase):
    url = "http://localhost:8011/"
    headers = {'Content-type': 'application/json'}
    path = os.path.abspath(os.path.dirname(__file__))

    @classmethod
    def setUpClass(cls):
        cls.server = Popen(['python', cls.path+'/server.py'])
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        DB().reset()
        cls.server.kill()

    def setUp(self):
        DB().reset()

    def nova_conta(self):
        return {'codigoVenda': 1,
                'dataVencimento': '05/06/2015',
                'dataPagamento': '06/05/2015',
                'status': 'PENDENTE'}

    def conta_1(self):
        return dict(self.nova_conta(), **{'codigo':1})

    def post(self, path, data):
        return requests.post(self.url+path, data, headers=self.headers)

    def get(self, path):
        return requests.get(self.url+path)

    def delete(self, path):
        return requests.delete(self.url+path)

    def test_cadastra_conta(self):
        conta = json.dumps(self.nova_conta())
        resposta = self.post('contas_a_receber', conta)
        self.assertEqual(
            DB().get('1'), self.conta_1()
        )

    def test_consulta_conta_por_codigo(self):
        DB().adicionar(self.nova_conta())
        resposta = self.get('contas_a_receber/1')
        self.assertEqual(
            self.conta_1(), resposta.json()
        )

    def test_consulta_conta_nao_existente_por_codigo(self):
        self.assertEqual(
            self.get('contas_a_receber/200').status_code, 404
        )

    def test_remove_conta(self):
        DB().adicionar(self.nova_conta())
        self.delete('contas_a_receber/1')
        self.assertEqual(DB().get('1'), None)

if __name__ == '__main__':
    unittest.main()
