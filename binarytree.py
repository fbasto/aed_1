import csv
import time

class Node():
   def __init__(self, init_ctry_name, init_ctry_code):
      self.ctry_name = init_ctry_name
      self.ctry_code = init_ctry_code
      self.ctry_pop = {} 
      for i in range(0,57):
         self.ctry_pop[1960+i] = None
      self.height=0   
      self.rightChild= None
      self.leftChild=None

   def get_ctry_name(self):
      return self.ctry_name
   def get_ctry_code(self):
      return self.ctry_code
   def get_ctry_pop(self):
      return self.ctry_pop
   def set_ctry_name(self, new_ctry_name):
      self.ctry_name = newctry_name
   def set_ctry_code(self, new_ctry_code):
      self.ctry_code = newctry_code
   def nodeprint(self):
      print(self.ctry_name,self.ctry_code,end=' ')
      print(self.ctry_pop)

class BinaryTree():
   def __init__(self):
      self.node = None

   def add(self,init_ctry_name, init_ctry_code):
      tree = self.node

      newnode = Node(init_ctry_name, init_ctry_code)

      if tree == None:
         self.node = newnode
         self.node.leftChild = BinaryTree()
         self.node.rightChild = BinaryTree()
      elif init_ctry_name < tree.ctry_name:
         self.node.leftChild.add(init_ctry_name, init_ctry_code)
      elif init_ctry_name > tree.ctry_name:
         self.node.rightChild.add(init_ctry_name, init_ctry_code)
      elif init_ctry_name == tree.ctry_name:
         return self.node

      return self.node


   def remove(self, ctry_name):
      if self.node != None:
         if self.node.ctry_name == ctry_name:
            if self.node.leftChild.node == None and self.node.rightChild.node == None:
               self.node = None
            elif self.node.leftChild.node == None:
               self.node = self.node.rightChild.node
            elif self.node.rightChild.node == None:
               self.node = self.node.leftChild.node
            else:
               tmp=find_min(self.node.rightChild.node)
               self.node.ctry_name=tmp.ctry_name
               remove_min(self.node.rightChild.node)

         elif ctry_name < self.node.ctry_name:
             self.node.leftChild.remove(ctry_name)
         elif ctry_name > self.node.ctry_name:
             self.node.rightChild.remove(ctry_name)
      else:
         return

   def find_min(self):
      #retornar min da subarvore direita do no a remover
      if self.node.leftChild.node is None:
         return self.node
      else:
         return find_min(self.node.leftChild.node)

   def remove_min(self):
      if self.node.leftChild.node is None:
         return self.node.rightChild.node
      else:
         self.node.leftChild.node = remove_min(self.node.leftChild.node)
         return self.node

   def find(self,ctry_name):
      print("nome ",ctry_name)
      if self.node == None:
         print("yo")
         return None
      elif ctry_name < self.node.ctry_name:
         self.node.leftChild.find(ctry_name)
      elif ctry_name > self.node.ctry_name:
         self.node.rightChild.find(ctry_name) 
      return self.node

   def traverse(self, visit, order='pre'):
      if order == 'pre':
         visit(self.node)
      if self.node.leftChild.node is not None:
         self.node.leftChild.traverse(visit, order)
      if order == 'in':
         visit(self.node)
      if self.node.rightChild.node is not None:
         self.node.rightChild.traverse(visit, order)
      if order == 'post':
         visit(self.node)

   def carregarDados(self):
      with open('dados.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
            #Cada row = Cada país
            row=', '.join(row)
            row=row.split(';')
            aux = self.add(row[0],row[1])
            print(aux.ctry_name,'!!',aux.ctry_code)
            for n in range(2,len(row)):
               #Cada n = index de celula de pops
               aux.get_ctry_pop()[1960+n-2] = row[n]


if __name__ == "__main__": 
   bts = BinaryTree()
   timer = False
   bts.carregarDados()
   bts.traverse(print,'in')
   while(True):
      print("\nTemporizador de operações:",timer)
      userop = eval(input("1-Pesquisa\n2-Insercao\n3-Edicao\n4-Remocao\n5-Fechar\n6-Ligar/Desligar temporizador de operações\n"))
      if(userop == 1):  #PESQUISA
         usercrit = eval(input("1-Pesquisa por nome\n2-Pesquisa por sigla\n"))
         usertext = input("Inserir palavra: ")
         start=time.time()
         if(usercrit == 1):
            aux = bts.find(usertext)
         if(usercrit == 2):
            aux = bts.findCode(usertext)
         if(aux != None):
            aux.nodeprint()
         if(timer is True):
            end=time.time()
            print("Operacao demorou: %.10f segundos" %(end-start))

      if(userop == 2):  #INSERCAO
         # usercrit = eval(input("Pretende inserir todas as percentagem da populacao portuguesa com acesso a rede eletrica? 1-Sim 2-Não"))
         usertext = input("Indicar nome de país a inserir: ")
         usertext2 = input("Indicar codigo de país a inserir: ")
         start=time.time()
         bts.add(usertext,usertext2)
         if(timer is True):
            end=time.time()
            print("Operacao demorou: %.10f segundos" %(end-start))

      if(userop == 3):  #EDICAO  DE PERCENTAGEM
         usertext = input("Indicar nome do país de que se pretende alterar a percentagem: ")
         usertext2 = eval(input("Indicar ano que se pretende alterar (1960 a 2016 inclusive): "))
         usertext3 = eval(input("Indicar valor: "))
         start=time.time()
         aux = bts.find(usertext)
         if(aux != None):
            aux.get_ctry_pop()[usertext2] = usertext3
         if(timer is True):
            end=time.time()  
            print("Operacao demorou: %.10f segundos" %(end-start))

      if(userop == 4):  #REMOCAO
         usercrit = eval(input("1-Remover país da lista\n2-Remover percentagem de um país-ano\n"))
         if(usercrit == 1):
            usertext = input("Indicar nome de país que se pretende remover: ")
            start=time.time()
            bts.remove(usertext)
            if(timer is True):
               end=time.time()
               print("Operacao demorou: %.10f segundos" %(end-start))
         if(usercrit == 2):
            usertext = input("Indicar nome do país do qual se pretende remover uma percentagem: ")
            usertext2 = eval(input("Indicar o ano do qual se pretende remover uma percentagem: "))
            start=time.time()
            aux = bts.find(usertext)
            if(aux != None):
               aux.get_ctry_pop()[usertext2] = None
            if(timer is True):
               end=time.time()
               print("Operacao demorou: %.10f segundos" %(end-start))
      if(userop == 5):
         break
      if(userop == 6):
         if(timer is False):
            timer = True
         else:
            timer = False