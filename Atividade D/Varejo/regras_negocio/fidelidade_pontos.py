# -*- coding:utf-8 -*_

from promocao import Promocao

class Fidelidade1000Pontos(Promocao):

	def descontar(self,compra):
		if compra.cliente.pontos >= 1000:
			desconto = compra.calcula_total() * 0.05

			pontos_atual = compra.cliente.pontos - 1000
			compra.cliente.pontos = pontos_atual
		else:
			desconto = 0
			
		return desconto