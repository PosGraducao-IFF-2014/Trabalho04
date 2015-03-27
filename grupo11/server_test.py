# -*- coding: utf-8 -*-
import json, requests, unittest
from models import DB

class ServerTest(unittest.TestCase):
    url = "http://localhost:8011"

    def test_cadastrar_contas_a_receber(self):
        conta = json.dumps(
            {'codigoVenda': 1,
             'dataVencimento': '05/06/2015',
             'dataPagamento': '06/05/2015',
             'status': 'PENDENTE'}
        )
        headers = {'Content-type': 'application/json'}
        resposta = requests.post(self.url+"/contas_a_receber",
            conta, headers=headers)
        self.assertTrue(
            DB()[0] == json.loads(conta)
        )

if __name__ == '__main__':
    unittest.main()
