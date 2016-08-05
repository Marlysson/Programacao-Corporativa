# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from implementacaoDAO import DAOImplementParticipante
from modelo import Participante

# Gerar tabelas
# Base.metadata.create_all(conexao)

conexao = create_engine("sqlite:///inicio.db")

#Criando a sessão ( Factory de conexões)
Sessao_db = sessionmaker(bind=conexao)
sessao = Sessao_db()

dao = DAOImplementParticipante(sessao)

todos = dao.findAll()

for p in todos:
	print(p.nome)