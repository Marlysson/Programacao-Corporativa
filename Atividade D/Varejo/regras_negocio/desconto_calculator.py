# -*- coding:utf-8 -*_

from promocao import Promocao

from compra_cara import *
from fidelidade_pontos import *

class DescontoCalculator():
	def calcula_desconto_total(self, compra):
		cc = ValorMaior1000Reais()
		fp = Fidelidade1000Pontos()
		#TODO Implementar A questao dos Items
		#TODO Implementar TESTES
		return cc.descontar() + fp.descontar()

	def calcula_valor_menos_desconto(self, compra):
		valor = compra.calcula_total()
		return valor - self.calcula_desconto_total(compra)