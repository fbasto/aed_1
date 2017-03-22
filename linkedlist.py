import csv
import time

class Node:
   def __init__(self, init_ctry_name, init_ctry_code):
      self.ctry_name = init_ctry_name
      self.ctry_code = init_ctry_code
      self.ctry_pop = {}
      for i in range(0,57):
         self.ctry_pop[1960+i] = ''
      self.next = None
   def get_ctry_name(self):
      return self.ctry_name
   def get_ctry_code(self):
      return self.ctry_code
   def get_ctry_pop(self):
      return self.ctry_pop
   def get_next(self):
         return self.next
   def set_ctry_name(self, new_ctry_name):
      self.ctry_name = newctry_name
   def set_ctry_code(self, new_ctry_code):
      self.ctry_code = newctry_code
   def set_next(self, new_next):
      self.next = new_next   
   def nodeprint(self):
       print(self.ctry_name,self.ctry_code,end=' ')
       print(self.ctry_pop)

         

class LinkedList:
   def __init__(self):
      self.head = None
   def is_empty(self):
      return self.head == None
   def add(self, ctry_name, ctry_code):
      temp = Node(ctry_name, ctry_code)
      temp.set_next(self.head)
      self.head = temp
      return self.head     
   def remove(self, item):
      current = self.head
      previous = None
      found = False
      while not found:
         if current.get_ctry_name() == item:
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
   
   def print_list(self):
      print("PRINTING LINKED LIST")
      currentNode = self.head
      if currentNode == None:
         return 0
      print(currentNode.nodeprint())
      while currentNode != None:
         currentNode = currentNode.get_next()
         if currentNode != None:
            # print(currentNode.get_ctry_name())
            currentNode.nodeprint()

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
      while(aux.get_ctry_name() != elem and aux.get_next() != None):
         aux = aux.get_next()
      if(aux.get_ctry_name() == elem):
         print("Encontrou", elem)
         return aux
      else:
         print("O pais",elem,"não foi encontrado")
         return None
   
   def findCode(self, elem):
      aux = self.head
      while(aux.get_ctry_code() != elem and aux.get_next() != None):
         aux = aux.get_next()
      if(aux.get_ctry_code() == elem):
         print("Encontrou ", elem)
         return aux
      else:
         print("O codigo de pais",elem,"não foi encontrado")
         return None


   def removeDuplicates(self):
      aux = self.head
      while(aux.get_next() != None):
         if(aux.get_ctry_name() == aux.get_next().get_ctry_name()):
            self.remove(aux.get_ctry_name())
            print("Removed duplicate of",aux.get_ctry_name())
         aux = aux.get_next()

   def carregarDados(self):
      with open('dados.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
            #Cada row = Cada país
            row=', '.join(row)
            row=row.split(';')
            aux = self.add(row[0],row[1])
            for n in range(2,len(row)):
               #Cada n = index de celula de pops
               aux.get_ctry_pop()[1960+n-2] = row[n]



if __name__ == "__main__": 
	l = LinkedList()
	# timer = False
	start=time.time()
	while(True):
		# print("\nTemporizador de operações:",timer)
		userop = eval(input("1-Pesquisa\n2-Insercao\n3-Edicao\n4-Remocao\n5-Fechar\n6-Ligar/Desligar temporizador de operações\n7-Carregar Dados\n"))
		if(userop == 1):  #PESQUISA
			usercrit = eval(input("1-Pesquisa por nome\n2-Pesquisa por sigla\n"))
			usertext = input("Inserir palavra: ")
			# start=time.time()
			if(usercrit == 1):
				aux = l.find(usertext)
			if(usercrit == 2):
				aux = l.findCode(usertext)
			if(aux != None):
				aux.nodeprint()
			# if(timer is True):
			#    end=time.time()
			#    print("Operacao demorou: %.10f segundos" %(end-start))
		if(userop == 2):  #INSERCAO
			# usercrit = eval(input("Pretende inserir todas as percentagem da populacao portuguesa com acesso a rede eletrica? 1-Sim 2-Não"))
			usertext = input("Indicar nome de país a inserir: ")
			usertext2 = input("Indicar codigo de país a inserir: ")
			# start=time.time()
			l.add(usertext,usertext2)
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
			aux = l.find(usertext)
			if(aux != None):
				aux.get_ctry_pop()[usertext2] = usertext3
				# if(timer is True):
				#    end=time.time()  
				#    print("Operacao demorou: %.10f segundos" %(end-start))
		if(userop == 4):  #REMOCAO
			usercrit = eval(input("1-Remover país da lista\n2-Remover percentagem de um país-ano\n"))
			if(usercrit == 1):
				usertext = input("Indicar nome de país que se pretende remover: ")
				# start=time.time()
				l.remove(usertext)
				# if(timer is True):
				#    end=time.time()
				#    print("Operacao demorou: %.10f segundos" %(end-start))
			if(usercrit == 2):
				usertext = input("Indicar nome do país do qual se pretende remover uma percentagem: ")
				usertext2 = eval(input("Indicar o ano do qual se pretende remover uma percentagem: "))
				# start=time.time()
				aux = l.find(usertext)
			if(aux != None):
				aux.get_ctry_pop()[usertext2] = ''
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
			l.carregarDados()
	end=time.time()
	print("Operacao demorou: %.10f segundos" %(end-start))


#Timer
# start=time.time()
# end=time.time()
# print("Operacao demorou: %.10f segundos" %(end-start))