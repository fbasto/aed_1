import csv
import time

class BinaryTree():
   def __init__(self, init_ctry_name, init_ctry_code):
      self.ctry_name = init_ctry_name
      self.ctry_code = init_ctry_code
      self.ctry_pop = {} 
      for i in range(0,57):
         self.ctry_pop[1960+i] = None
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


   #descobre o menor elemento da subarvore direita, copia os dados para o nó atual e é removido
   def remove(self,ctry_name):
      if ctry_name < self.ctry_name:
         self.leftChild = self.leftChild.remove(ctry_name)
      elif ctry_name > self.ctry_name:
         self.rightChild = self.rightChild.remove(ctry_name)
      else:
         if self.rightChild is None:
            return self.leftChild
         if self.leftChild is None:
            return self.rightChild
         aux = self.rightChild.find_min()
         self.ctry_name=aux.ctry_name
         self.ctry_code=aux.ctry_code
         self.ctry_pop=aux.ctry_pop
         self.rightChild = self.rightChild.remove_min()
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
            print(row[0],row[1])
            aux = self.add(row[0],row[1])
            for n in range(2,len(row)):
               #Cada n = index de celula de pops
               aux.get_ctry_pop()[1960+n-2] = row[n]
            #print(aux.ctry_name,'!!',aux.ctry_code)
            #print(aux.get_ctry_pop())

   def casoTeste(bts):
      bts.add("Austria","AT")
      bts.add("Portugal","PT")
      bts.add("Espana","ET")
      bts.add("se","dT")
      bts.add("fs","sT")
      bts.add("Alemanha","al")
      bts.remove("Nome")
      #bts.remove("s")
      bts.printTree()

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
  
   bts.casoTeste()

   
   