import csv
import time
from linkedlistaux import *


class BinaryTree():
   def __init__(self,info):
      self.key= info
      self.pointer= None
      self.list = None
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
   def nodeprint(self,usercrit):
      if usercrit == 1:
          print(self.key,self.pointer.key,end=' ')
          print(self.list.print_list())
      elif usercrit == 2:
          print(self.pointer.key,self.key,end=' ')
          print(self.pointer.list.print_list())  


   def find(self,key):
      if key< self.key:
         if self.leftChild != None:
            return self.leftChild.find(key)
         else:
            return None
      elif key> self.key:
         if self.rightChild != None:
            return self.rightChild.find(key)
         else:
            return None
      else:
         return self


    
   """
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
   """

   def add(self,newnode):
      if self.key > newnode.key:
         if self.leftChild is None:
            self.leftChild = newnode
         else:
            self.leftChild.add(newnode)
      elif self.key< newnode.key:
         if self.rightChild is None:
            self.rightChild = newnode 
         else:
            self.rightChild.add(newnode)
      else:
         print("Nó já existe na árvore!")
      return newnode


   #descobre o menor elemento da subarvore direita, copia os dados para o nó atual e é removido
   def remove(self,key):
      if key < self.key and self.leftChild != None:
         self.leftChild = self.leftChild.remove(key)
      elif key > self.key and self.rightChild != None:
         self.rightChild = self.rightChild.remove(key)
      elif key == self.key:
         if self.rightChild is None:
            return self.leftChild
         if self.leftChild is None:
            return self.rightChild
         aux = self.rightChild.find_min()
         self.key = aux.key
         self.pointer = aux.pointer
         self.list = aux.list
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

#nome e sigla
def createNode(key1,key2): 
    llist = AuxiliarLinkedList()
    aux_name_node = BinaryTree(key1)
    aux_sig_node = BinaryTree(key2)
    aux_name_node.pointer = aux_sig_node
    aux_name_node.list = llist 
    aux_sig_node.pointer = aux_name_node
    return aux_name_node,aux_sig_node

def carregarDados():
    with open('dados.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #f = open('remocao264.txt', 'w')
        #num = 0
        for row in spamreader:
            #Cada row = Cada país
            row=', '.join(row)
            row=row.split(';')
            aux_name,aux_sig = createNode(row[0],row[1])
            for n in range(2,len(row)):
                #Cada n = index de celula de pops
                #no.get_ctry_pop()[1960+n-2] = row[n]
                aux_name.list.find(1960+n-2).set_pop(row[n])
                #self.display()
            aux = bstname.add(aux_name)
            aux1 = bstsigla.add(aux_sig)

def carregarDados2():
    with open('dados132.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #f = open('remocao264.txt', 'w')
        #num = 0
        for row in spamreader:
            #Cada row = Cada país
            row=', '.join(row)
            row=row.split(';')
            aux_name,aux_sig = createNode(row[0],row[1])
            for n in range(2,len(row)):
                #Cada n = index de celula de pops
                #no.get_ctry_pop()[1960+n-2] = row[n]
                aux_name.list.find(1960+n-2).set_pop(row[n])
                #self.display()
            aux = bstname.add(aux_name)
            aux1 = bstsigla.add(aux_sig)



if __name__ == "__main__": 
   bstname = BinaryTree("Nome")
   bstsigla = BinaryTree("Nome")
   # timer = False
   
   carregarDados()
   start = time.time()
   while(True):
      # print("\nTemporizador de operações:",timer)
      userop = eval(input("1-Pesquisa\n2-Insercao\n3-Edicao\n4-Remocao\n5-Fechar\n6-Ligar/Desligar temporizador de operações\n7-Carregar Dados\n8-Carregar metade dos Dados\n"))
      if(userop == 1):  #PESQUISA
         usercrit = eval(input("1-Pesquisa por nome\n2-Pesquisa por sigla\n"))
         usertext = input("Inserir palavra: ")
         # start=time.time()
         if(usercrit == 1):
            aux = bstname.find(usertext)
         if(usercrit == 2):
            aux = bstsigla.find(usertext)
         if(aux != None):
            aux.nodeprint(usercrit)
         else:
            print("Nao existe")
         # if(timer is True):
         #    end=time.time()
         #    print("Operacao demorou: %.10f segundos" %(end-start))

      if(userop == 2):  #INSERCAO
         # usercrit = eval(input("Pretende inserir todas as percentagem da populacao portuguesa com acesso a rede eletrica? 1-Sim 2-Não"))
         usertext = input("Indicar nome de país a inserir: ")
         usertext2 = input("Indicar codigo de país a inserir: ")
         # start=time.time()
         aux_name,aux_sig = createNode(usertext,usertext2)
         bstname.add(aux_name)
         bstsigla.add(aux_sig)
         # if(timer is True):
         #    end=time.time()
         #    print("Operacao demorou: %.10f segundos" %(end-start))

      if(userop == 3):  #EDICAO  DE PERCENTAGEM

         usertext = input("Indicar nome do país de que se pretende alterar a percentagem: ")
         usertext2 = eval(input("Indicar ano que se pretende alterar (1960 a 2016 inclusive): "))
         usertext3 = eval(input("Indicar valor: "))
         # start=time.time()
         aux = bstname.find(usertext)
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
            bstsigla.remove(bstname.find(usertext).pointer.key)
            bstname.remove(usertext)
            # if(timer is True):
            #    end=time.time()
            #    print("Operacao demorou: %.10f segundos" %(end-start))
         if(usercrit == 2):
            usertext = input("Indicar nome do país do qual se pretende remover uma percentagem: ")
            usertext2 = eval(input("Indicar o ano do qual se pretende remover uma percentagem: "))
            # start=time.time()
            aux = bstname.find(usertext)
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
         carregarDados()
         cdend=time.time()
         print("Carregar dados demorou: %.10f segundos" %(cdend-cdstart))
      if(userop == 8):
         cdstart = time.time()
         carregarDados2()
         cdend=time.time()
         print("Carregar metade dos dados demorou: %.10f segundos" %(cdend-cdstart))
   end=time.time()
   print("Operacao demorou: %.10f segundos" %(end-start))
   
   
