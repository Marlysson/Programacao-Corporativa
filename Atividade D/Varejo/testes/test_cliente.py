# -*- coding: utf-8 -*_

import unittest
import sys,os

#Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.cliente import Cliente

class TestaCliente(unittest.TestCase):

	def test_cliente(self):
		cliente = Cliente("Marlysson")

		self.assertEqual(cliente.nome,"Marlysson")

if __name__ == "__main__":
	unittest.main()