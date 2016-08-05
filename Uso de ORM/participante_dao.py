# -*- coding:utf-8 -*-

from dao import dao
from modelo import Participante

class ParticipanteDAO(dao):

	def __init__(self,sessao):
		self.session = sessao

	def save(self,objeto):
		self.session.add(objeto)
		self.session.commit()

	def delete(self,objeto):
		if self.find(objeto.id):
			participante_removido = self.session.query(Participante).filter_by(id=objeto.id).delete()
		else:
			raise Exception("Participante não encontrado.")

	def find(self,id):
		participante = self.session.query(Participante).filter_by(id=id).all()
		return participante

	def findAll(self):
		todos = self.session.query(Participante).all()
		return todos
		