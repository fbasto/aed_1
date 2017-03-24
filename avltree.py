import csv
import time
from random import randint
from linkedlistaux import *

class Node:
    def __init__(self, info):
      self.key=info 
      self.pointer= None
      self.list= None
      self.rightChild= None
      self.leftChild=None

    def get_ctry_name(self):
      return self.ctry_name
    def get_ctry_code(self):
      return self.ctry_code
    def get_next(self):
        return self.next
    def get_ctry_pop(self):
      return self.ctry_pop
    def set_ctry_name(self, new_ctry_name):
      self.ctry_name = newctry_name
    def set_ctry_code(self, new_ctry_code):
      self.ctry_code = newctry_code
    def set_next(self, new_next):
      self.next = new_next
    def nodeprint(self,usercrit):
        if usercrit == 1:
            print(self.key,self.pointer.key,end=' ')
            print(self.list.print_list())
        elif usercrit == 2:
            print(self.pointer.key,self.key,end=' ')
            print(self.pointer.list.print_list()) 



class AVLTree:
    def __init__(self, *args):
       self.node = None
       self.height = -1
       self.balance = 0


    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self,newnode):
        tree = self.node
        if tree == None:
            self.node = newnode
            self.node.leftChild = AVLTree()
            self.node.rightChild = AVLTree()
        elif newnode.key< tree.key:
            self.node.leftChild.insert(newnode)
        elif newnode.key> tree.key:
            self.node.rightChild.insert(newnode)

        self.rebalance()
        return self.node
        

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.leftChild.balance < 0:
                    self.node.leftChild.lrotate()
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
            if self.balance < -1:
                if self.node.rightChild.balance > 0:
                    self.node.rightChild.rrotate()
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


    def rrotate(self):
        A = self.node
        B = self.node.leftChild.node
        T = B.rightChild.node

        self.node = B
        B.rightChild.node = A
        A.leftChild.node = T

    def lrotate(self):
        A = self.node
        B = self.node.rightChild.node
        T = B.leftChild.node

        self.node = B
        B.leftChild.node = A
        A.rightChild.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.leftChild != None:
                    self.node.leftChild.update_heights()
                if self.node.rightChild != None:
                    self.node.rightChild.update_heights()

            self.height = max(self.node.leftChild.height,self.node.rightChild.height) + 1
        else:
            self.height = -1


    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.leftChild != None:
                    self.node.leftChild.update_balances()
                if self.node.rightChild != None:
                    self.node.rightChild.update_balances()

            self.balance = self.node.leftChild.height - self.node.rightChild.height
        else:
            self.balance = 0


    def remove(self,key):
        if self.node != None:
            if self.node.key == key:
                if self.node.leftChild.node == None and self.node.rightChild.node == None:
                    self.node = None
                elif self.node.leftChild.node == None:
                    self.node = self.node.rightChild.node
                elif self.node.rightChild.node == None:
                    self.node = self.node.leftChild.node

                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:
                        self.node.key = replacement.key

                        self.node.rightChild.remove(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.leftChild.remove(key)
            elif key > self.node.key:
                self.node.rightChild.remove(key)

            self.rebalance()
        else:
            return


    def logical_predecessor(self,node):
        node = node.leftChild.node
        if node != None:
            while node.rightChild != None:
                if node.rightChild.node == None:
                    return node
                else:
                    node = node.rightChild.node
        return node




    def logical_successor(self,node):
        node = node.rightChild.node
        if node != None: # just a sanity check

            list = LinkedList()
            while node.leftChild != None:
                if node.leftChild.node == None:
                    return node
                else:
                    node = node.leftChild.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.leftChild.check_balanced() and self.node.rightChild.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.leftChild.inorder_traverse()
        for i in l:
            inlist.append(i)
        #em ordem por nome do pais mas tmb pode ser pelo codigo
        inlist.append(self.node.ctry_name)

        l = self.node.rightChild.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def find(self,key):
        if self.node == None:
            return None
        if key < self.node.key:
            if self.node.leftChild != None:
                return self.node.leftChild.find(key)
            else:
                return None
        elif key > self.node.key:
            if self.node.rightChild != None:
                return self.node.rightChild.find(key)
            else:
                return None
        else:
            return self.node

    """def findCode(self,ctry_code):
        if self.node == None:
            return None
        if ctry_code < self.node.ctry_code:
            if self.node.leftChild != None:
                return self.node.leftChild.findCode(ctry_code)
            else:
                return None
        elif ctry_code > self.node.ctry_code:
            if self.node.rightChild != None:
                return self.node.rightChild.findCode(ctry_code)
            else:
                return None
        else:
            return self.node
    """

    

    """
    def carregarDados2(self):
      with open('dados132.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
            #Cada row = Cada país
            row=', '.join(row)
            row=row.split(';')
            aux = self.insert(row[0],row[1])
            no = self.find(row[0])
            for n in range(2,len(row)):
               #Cada n = index de celula de pops
               no.get_ctry_pop()[1960+n-2] = row[n]
            #self.display()
    """
    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if(self.node != None):
            print ('-' * level * 2, pref, self.node.ctry_name, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.leftChild != None:
                self.node.leftChild.display(level + 1, '<')
            if self.node.leftChild != None:
                self.node.rightChild.display(level + 1, '>')

if __name__ == "__main__":
   nametree = AVLTree()
   siglatree = AVLTree()
   
   with open('dados.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     #f = open('remocao264.txt', 'w')
     num = 0
     for row in spamreader:
        #Cada row = Cada país
        llist = AuxiliarLinkedList()
        row=', '.join(row)
        row=row.split(';')
        aux_name_node = Node(row[0])
        aux_sig_node = Node(row[1])
        aux_name_node.pointer = aux_sig_node
        aux_name_node.list = llist 
        aux_sig_node.pointer = aux_name_node
        for n in range(2,len(row)):
            #Cada n = index de celula de pops
            #no.get_ctry_pop()[1960+n-2] = row[n]
            aux_name_node.list.find(1960+n-2).set_pop(row[n])
            #self.display()
        aux = nametree.insert(aux_name_node)
        #no = self.find(row[0])

   # timer = False
   start=time.time()
   while(True):
      # print("\nTemporizador de operações:",timer)
      userop = eval(input("1-Pesquisa\n2-Insercao\n3-Edicao\n4-Remocao\n5-Fechar\n6-Ligar/Desligar temporizador de operações\n7-Carregar Dados\n8-Carregar metade dos Dados\n"))
      if(userop == 1):  #PESQUISA
         usercrit = eval(input("1-Pesquisa por nome\n2-Pesquisa por sigla\n"))
         usertext = input("Inserir palavra: ")
         # start=time.time()
         if(usercrit == 1):
            aux = nametree.find(usertext)
         if(usercrit == 2):
            aux = siglatree.find(usertext)
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
         t.insert(usertext,usertext2)
         # if(usercrit == 1):
         #    aux = t.insert(usertext,usertext2)
         #    for n in range(0,57):
         #       aux.get_ctry_pop()[1960+n] = input("Percentagem populacao em ",1960+n,": ")
         # if(usercrit == 2):
         #    t.insert(usertext,usertext2)
         # if(timer is True):
         #    end=time.time()
         #    print("Operacao demorou: %.10f segundos" %(end-start))

      if(userop == 3):  #EDICAO  DE PERCENTAGEM
         usertext = input("Indicar nome do país de que se pretende alterar a percentagem: ")
         usertext2 = eval(input("Indicar ano que se pretende alterar (1960 a 2016 inclusive): "))
         usertext3 = eval(input("Indicar valor: "))
         # start=time.time()
         aux = t.find(usertext)
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
            t.remove(usertext)
            # if(timer is True):
            #    end=time.time()
            #    print("Operacao demorou: %.10f segundos" %(end-start))
         if(usercrit == 2):
            usertext = input("Indicar nome do país do qual se pretende remover uma percentagem: ")
            usertext2 = eval(input("Indicar o ano do qual se pretende remover uma percentagem: "))
            # start=time.time()
            aux = t.find(usertext)
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
         cdstart = time.time()
         t.carregarDados()
         cdend=time.time()
         print("Carregar dados demorou: %.10f segundos" %(cdend-cdstart))
      if(userop == 8):
         cdstart = time.time()
         t.carregarDados2()
         cdend=time.time()
         print("Carregar metade dos dados demorou: %.10f segundos" %(cdend-cdstart))
   end=time.time()
   print("Operacao demorou: %.10f segundos" %(end-start))
