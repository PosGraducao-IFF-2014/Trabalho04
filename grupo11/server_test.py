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
        DB().reset()
        cls.server = Popen(['python', cls.path+'/server.py'])
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        DB().reset()
        cls.server.kill()

    def conta_a_receber(self):
        return {'codigoVenda': 1,
                'dataVencimento': '05/06/2015',
                'dataPagamento': '06/05/2015',
                'status': 'PENDENTE'}

    def post(self, path, data):
        return requests.post(self.url+path, data, headers=self.headers)

    def get(self, path):
        return requests.get(self.url+path)

    def test_cadastra_conta(self):
        conta = json.dumps(self.conta_a_receber())
        resposta = self.post('contas_a_receber', conta)
        self.assertEqual(
            DB()[0], json.loads(conta)
        )

    def test_consulta_conta_por_codigo(self):
        DB().reset(); DB().adicionar(self.conta_a_receber())
        resposta = self.get('contas_a_receber/1')
        self.assertEqual(
            self.conta_a_receber(), resposta.json()
        )

    def test_consulta_conta_nao_existente_por_codigo(self):
        self.assertEqual(
            self.get('contas_a_receber/200').status_code, 404
        )

if __name__ == '__main__':
    unittest.main()
