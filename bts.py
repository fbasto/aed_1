import csv
import time

class BinaryTree():
   def __init__(self, init_ctry_name, init_ctry_code):
      self.ctry_name = init_ctry_name
      self.ctry_code = init_ctry_code
      self.ctry_pop = {} 
      for i in range(0,57):
         self.ctry_pop[1960+i] = ''
      self.rightChild= None
      self.leftChild=None


   def get_rightChild(self):
      return self.rightChild
   def get_leftChild(self):
      return self.leftChild
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


   def find(self,ctry_name):
      if ctry_name < self.ctry_name:
         if self.leftChild != None:
            return self.leftChild.find(ctry_name)
         else:
            return None
      elif ctry_name > self.ctry_name:
         if self.rightChild != None:
            return self.rightChild.find(ctry_name)
         else:
            return None
      else:
         return self

   def findCode(self,ctry_code):
      if ctry_code < self.ctry_code:
         if self.leftChild != None:
            return self.leftChild.findCode(ctry_code)
         else:
            return None
      elif ctry_code > self.ctry_code:
         if self.rightChild != None:
            return self.rightChild.findCode(ctry_code)
         else:
            return None
      else:
         return self


   def add(self,init_ctry_name, init_ctry_code):
      no = BinaryTree(init_ctry_name, init_ctry_code)
      if self.ctry_name > no.ctry_name:
         if self.leftChild is None:
            self.leftChild = no
         else:
            self.leftChild.add(init_ctry_name,init_ctry_code)
      elif self.ctry_name < no.ctry_name:
         if self.rightChild is None:
            self.rightChild = no
         else:
            self.rightChild.add(init_ctry_name,init_ctry_code)
      else:
         print("Nó já existe na árvore!")
      return no


   #descobre o menor elemento da subarvore direita, copia os dados para o nó atual e é removido
   def remove(self,ctry_name):
      if ctry_name < self.ctry_name and self.leftChild != None:
         self.leftChild = self.leftChild.remove(ctry_name)
      elif ctry_name > self.ctry_name and self.rightChild != None:
         self.rightChild = self.rightChild.remove(ctry_name)
      elif ctry_name == self.ctry_name:
         if self.rightChild is None:
            return self.leftChild
         if self.leftChild is None:
            return self.rightChild
         aux = self.rightChild.find_min()
         self.ctry_name=aux.ctry_name
         self.ctry_code=aux.ctry_code
         self.ctry_pop=aux.ctry_pop
         self.rightChild = self.rightChild.remove_min()
      else: 
         print("Nó não existe!")
         return
      return self

   def find_min(self):
      if self.leftChild is None:
         return self
      else:
         return self.leftChild.find_min()

   def remove_min(self):
      if self.leftChild is None:
         return self.rightChild
      else:
         self.leftChild = self.leftChild.remove_min()
         return self


   def carregarDados(self):
      with open('dados.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
            #Cada row = Cada país
            row=', '.join(row)
            row=row.split(';')
            aux = self.add(row[0],row[1])
            no = self.find(row[0])
            for n in range(2,len(row)):
               #Cada n = index de celula de pops
               no.get_ctry_pop()[1960+n-2] = row[n]


   def printTree(self):
      if self == None:
         print("Árvore vazia!")
         return
      else:
         if self.leftChild!=None:
            self.leftChild.printTree()
         if self.rightChild!=None:
            self.rightChild.printTree()
         print(self.ctry_name,"|",self.ctry_code)

if __name__ == "__main__": 
   bts = BinaryTree("Nome","Código")
   timer = False
   bts.remove("Nome")
   bts.printTree()
   while(True):
      print("\nTemporizador de operações:",timer)
      userop = eval(input("1-Pesquisa\n2-Insercao\n3-Edicao\n4-Remocao\n5-Fechar\n6-Ligar/Desligar temporizador de operações\n7-Carregar Dados\n"))
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
         else:
            print("Nao existe")
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
               aux.get_ctry_pop()[usertext2] = ''
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
      if(userop == 7):
         l.carregarDados()

   
   