# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base

#Base para usar ORM
Base = declarative_base()

# Importando tipos para modelos
from sqlalchemy import Column , Integer , String

class Participante(Base):
	__tablename__ = "participante"

	id     = Column(Integer,primary_key=True)
	cpf    = Column(String)
	nome   = Column(String)
	fone   = Column(Integer)
	perfil = Column(String)

	def __repr__(self):
		template = "<Participante nome={}, cpf={} , fone={} , perfil={} >"

		return template.format(self.cpf,self.nome,self.fone,self.perfil)