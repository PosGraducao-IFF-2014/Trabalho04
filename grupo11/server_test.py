# -*- coding: utf-8 -*-
import json, requests, time, unittest
from subprocess import Popen
from models import DB

class ServerTest(unittest.TestCase):
    url = "http://localhost:8011"
    headers = {'Content-type': 'application/json'}

    @classmethod
    def setUpClass(cls):
        DB().reset()

    @classmethod
    def tearDownClass(cls):
        DB().reset()

    def post(self, path, data):
        return requests.post(self.url+path, data, headers=self.headers)

    def test_cadastrar_contas_a_receber(self):
        conta = json.dumps(
            {'codigoVenda': 1,
             'dataVencimento': '05/06/2015',
             'dataPagamento': '06/05/2015',
             'status': 'PENDENTE'}
        )
        resposta = self.post('/contas_a_receber', conta)
        self.assertTrue(
            DB()[0] == json.loads(conta)
        )


if __name__ == '__main__':
    unittest.main()
