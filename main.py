import sys
import random
countServers = int(sys.argv[2])
way = sys.argv[3]

listWithNumbers = []
for i in range(1,51):
	listWithNumbers.append(i)
	listWithNumbers.append(i)


class Server:
	"""Клас сервер, конструктор принимает количество серверов"""
	count = 0
	startMirror = -4
	endMirror = 1
	def __init__( self, counter):
		self.id = counter
		self.listCheakOnCopiesInOb = []
		if way == '--random':	
			self.shards = self.generateRandom()[:]
		elif way == '--mirror':
			self.shards = self.generateMirror()[:]		 
		self.__work = True
		Server.count += 1
		if Server.count == 2:
			Server.count = 0


	
	def show(self):
		print(self.shards)
	
	def generateRandom( self):
		"""функция генерирует рандомное размещение данных в первом случае"""
		listTemp = [] 
		for i in range(0, 10):	
			listTemp.append(self.checkForOb())
		return listTemp	

	def generateMirror(self):
		"""функция генерирует размещение данных во втором случае"""
		listTemp = []
		if Server.count == 0:
			Server.startMirror += 5
			Server.endMirror += 5
		for i in range( Server.startMirror, Server.endMirror ):	
			listTemp.append(i)
		return listTemp	

	def checkForOb(self):
		"""функция проверяет данные на сходство и берет рандомный данные для первого случая"""
		while True:
			if len(listWithNumbers) == 1:
				number = listWithNumbers[0]
			else: 
				number = listWithNumbers[random.randint(1,len(listWithNumbers) - 1)]
			if not number in self.listCheakOnCopiesInOb:
				listWithNumbers.remove(number)
				return number	

	def crashed(self):
		"""Функция для падения сервера"""
		self.__work = not self.__work



if __name__ == '__main__':
	serverList = []
	for i in range(0, countServers):
		serverList.append(Server(i))
	firstCrashed = 0;
	serverList[0].crashed()
	count = 0
	for i in range(0, countServers):
		if firstCrashed == i:
			continue
		serverList[i].crashed()
		for j in range(0, len( serverList[firstCrashed].shards )):
			if serverList[firstCrashed].shards[j] in serverList[i].shards:
				count += 1 	 
				break
		serverList[i].crashed()
	print("Killing 2 arbitrary servers results in data loss in {}% cases".format(round(count / (countServers - 1) * 100, 2))) 	
