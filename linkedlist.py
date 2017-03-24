import csv
import time
from linkedlistaux import *

class Node:
	def __init__(self, info):
		self.key = info
		self.pointer = None
		self.list = None
		self.next = None
		# self.ctry_name = init_ctry_name
		# self.ctry_code = init_ctry_code
		# self.ctry_pop = {}
		# for i in range(0,57):
		#    self.ctry_pop[1960+i] = ''
	def get_key(self):
		return self.key
	def get_next(self):
		return self.next
	def set_key(self, newinfo):
		self.key = newinfo
	def set_next(self, new_next):
		self.next = new_next
	def nodeprint(self,usercrit):
		if usercrit == 1:
			print(self.key,self.pointer.key,end=' ')
			print(self.list.print_list())
		elif usercrit == 2:
			print(self.pointer.key,self.key,end=' ')
			print(self.pointer.list.print_list())

         

class LinkedList:
   def __init__(self):
      self.head = None
   def is_empty(self):
      return self.head == None
   def add(self, info):
      temp = info
      temp.set_next(self.head)
      self.head = temp
      # print("added",temp.get_key())
      return self.head     
   def remove(self, item):
      current = self.head
      previous = None
      found = False
      while not found:
         if current.get_key() == item:
            found = True      
         else:
            previous = current
            current = current.get_next()
      if previous == None:
         self.head = current.get_next()
      else:
         previous.set_next(current.get_next())  
      if(found == False):
         print("O pais",elem,"não foi encontrado")
   
   def print_list(self,usercrit):
      print("PRINTING LINKED LIST")
      currentNode = self.head
      if currentNode == None:
         return 0     
      while currentNode != None:
         currentNode.nodeprint(usercrit)
         currentNode = currentNode.get_next()

   def size(self):
      aux = self.head
      if(aux != None):
         contador=1
      while(aux.get_next() != None):
         aux = aux.get_next()
         contador=contador+1
      return contador

   def find(self, elem):
      	aux = self.head
      	while(aux.get_key() != elem and aux.get_next() != None):
        	aux = aux.get_next()
      	if(aux.get_key() == elem):
        	print("Encontrou", elem)
        	return aux
      	else:
        	print("O pais",elem,"não foi encontrado")
        	return None

def createNode(key1,key2): 
    llist = AuxiliarLinkedList()
    aux_name_node = Node(key1)
    aux_sig_node = Node(key2)
    aux_name_node.pointer = aux_sig_node
    aux_name_node.list = llist 
    aux_sig_node.pointer = aux_name_node
    return aux_name_node,aux_sig_node


def carregarDados():
	with open('dados.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			#Cada row = Cada país
			row=', '.join(row)
			row=row.split(';')
			aux_name,aux_sig = createNode(row[0],row[1])
			for n in range(2,len(row)):
			#Cada n = index de celula de pops
				aux_name.list.find(1960+n-2).set_pop(row[n])
			aux = namelist.add(aux_name)
			aux1 = siglalist.add(aux_sig)

def carregarDados2():
	with open('dados132.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			#Cada row = Cada país
			row=', '.join(row)
			row=row.split(';')
			aux_name,aux_sig = createNode(row[0],row[1])
			for n in range(2,len(row)):
			#Cada n = index de celula de pops
				aux_name.list.find(1960+n-2).set_pop(row[n])
			aux = namelist.add(aux_name)
			aux1 = siglalist.add(aux_sig)



if __name__ == "__main__": 
	namelist = LinkedList()
	siglalist = LinkedList()

	# timer = False
	carregarDados()
	start=time.time()
	while(True):
		# print("\nTemporizador de operações:",timer)
		userop = eval(input("1-Pesquisa\n2-Insercao\n3-Edicao\n4-Remocao\n5-Fechar\n6-Ligar/Desligar temporizador de operações\n7-Carregar Dados\n8-Carregar metade dos Dados\n"))
		if(userop == 1):  #PESQUISA
			usercrit = eval(input("1-Pesquisa por nome\n2-Pesquisa por sigla\n"))
			usertext = input("Inserir palavra: ")
			# start=time.time()
			if(usercrit == 1):
				aux = namelist.find(usertext)
			if(usercrit == 2):
				aux = siglalist.find(usertext)
			if(aux != None):
				aux.nodeprint(usercrit)
			# if(timer is True):
			#    end=time.time()
			#    print("Operacao demorou: %.10f segundos" %(end-start))
		if(userop == 2):  #INSERCAO
			# usercrit = eval(input("Pretende inserir todas as percentagem da populacao portuguesa com acesso a rede eletrica? 1-Sim 2-Não"))
			usertext = input("Indicar nome de país a inserir: ")
			usertext2 = input("Indicar codigo de país a inserir: ")
			# start=time.time()
			aux_name,aux_sig = createNode(usertext,usertext2)
			namelist.add(aux_name)
			siglalist.add(aux_sig)
			# if(usercrit == 1):
			#    aux = l.add(usertext,usertext2)
			#    for n in range(0,57):
			#       aux.get_ctry_pop()[1960+n] = input("Percentagem populacao em ",1960+n,": ")
			# if(usercrit == 2):
			#    l.add(usertext,usertext2)
			# if(timer is True):
			#    end=time.time()
			#    print("Operacao demorou: %.10f segundos" %(end-start))
		if(userop == 3):  #EDICAO  DE PERCENTAGEM
			usertext = input("Indicar nome do país de que se pretende alterar a percentagem: ")
			usertext2 = eval(input("Indicar ano que se pretende alterar (1960 a 2016 inclusive): "))
			usertext3 = eval(input("Indicar valor: "))
			# start=time.time()
			aux = namelist.find(usertext)
			if(aux != None):
				aux.list.find(usertext2).set_pop(usertext3)
				# if(timer is True):
				#    end=time.time()  
				#    print("Operacao demorou: %.10f segundos" %(end-start))
		if(userop == 4):  #REMOCAO
			usercrit = eval(input("1-Remover país da lista\n2-Remover percentagem de um país-ano\n"))
			if(usercrit == 1):
				usertext = input("Indicar nome de país que se pretende remover: ")
				# start=time.time()
				siglalist.remove(namelist.find(usertext).pointer.key)
				namelist.remove(usertext)
				# if(timer is True):
				#    end=time.time()
				#    print("Operacao demorou: %.10f segundos" %(end-start))
			if(usercrit == 2):
				usertext = input("Indicar nome do país do qual se pretende remover uma percentagem: ")
				usertext2 = eval(input("Indicar o ano do qual se pretende remover uma percentagem: "))
				# start=time.time()
				aux = namelist.find(usertext)
				if(aux != None):
					aux.list.find(usertext2).set_pop('')
				# if(timer is True):
				#    end=time.time()
				#    print("Operacao demorou: %.10f segundos" %(end-start))
		if(userop == 5):
			break
		# if(userop == 6):
			# if(timer is False):
			#    timer = True
			# else:
			#    timer = False
		if(userop == 7):
			cdstart = time.time()
			l.carregarDados()
			cdend=time.time()
			print("Carregar dados demorou: %.10f segundos" %(cdend-cdstart))
		if(userop == 8):
			cdstart = time.time()
			l.carregarDados2()
			cdend=time.time()
			print("Carregar metade dos dados demorou: %.10f segundos" %(cdend-cdstart))
	end=time.time()
	print("Operacao demorou: %.10f segundos" %(end-start))


#Timer
# start=time.time()
# end=time.time()
# print("Operacao demorou: %.10f segundos" %(end-start))