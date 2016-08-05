# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database(object):

	_session = None

	def __init__(self,uri):
		self.uri = uri
		self._session = None

	def _conect(self):
		con = create_engine(self.uri)
		return con

	def _session(self):
		Session = sessionmaker(bind=self._conect())

		session_db = Session()

		return session_db
		
	def instance(self):
		if Database._session is None:
			Database._session = Database._session()

		return Database._session