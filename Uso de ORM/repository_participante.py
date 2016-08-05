# -*- coding : utf-8 -*-

class RepositoryParticipante(dao):

	def retornarCamposObjeto(self,id,campos):
		participante = self.session.query(Participante).filter_by(cpf=cpf).all()

		if not participante:
			raise Exception("Participante não encontrado")
		return participante

	def retornarPorCampos(self,nome):
		participante = self.session.query(Participante).filter_by(nome=nome)

		return participante