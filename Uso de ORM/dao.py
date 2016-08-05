# -*- coding : utf-8 -*-

from abc import ABCMeta

class DAO(metaclass=ABCMeta):

	@abc.abstractmethod
	def save(self,objeto):
		pass

	@abc.abstractmethod
	def delete(self,id):
		pass

	@abc.abstractmethod
	def find(self,id):
		pass

	@abc.abstractmethod
	def findAll(self):
		pass