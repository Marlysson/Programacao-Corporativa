# -*- coding : utf-8 -*-

from db import Database
import unittest


class TestDatabase(unittest.TestCase):

	def teste_singleton_de_conexao(self):
		db1 = Database("sqlite:///:memory:").instance()
		db2 = Database("sqlite:///:memory:").instance()

		self.assertEqual(id(db1),id(db2))


if __name__ == "__main__":
	unittest.main()