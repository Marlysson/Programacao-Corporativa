# -*- coding:utf-8 -*_

from promocao import Promocao

class ValorMaior1000Reais(Promocao):

	def descontar(self,compra):
		if compra.calcula_total() > 1000:
			desconto = compra.calcula_total() * 0.1
		else:
			desconto = 0

		return desconto