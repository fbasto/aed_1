import csv
outputdebug = False 

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, init_ctry_name, init_ctry_code):
      self.ctry_name = init_ctry_name
      self.ctry_code = init_ctry_code
      self.ctry_pop = {} 
      self.height=0   
      self.rightChild= None
      self.leftChild=None

    def get_ctry_name(self):
      return self.ctry_name
    def get_ctry_code(self):
      return self.ctry_code
    def get_next(self):
         return self.next
    def set_ctry_name(self, new_ctry_name):
      self.ctry_name = newctry_name
    def set_ctry_code(self, new_ctry_code):
      self.ctry_code = newctry_code
    def set_next(self, new_next):
      self.next = new_next   
    def print(self)
      print(,end='')
    


class AVLTree():
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

    def insert(self,init_ctry_name, init_ctry_code):
        tree = self.node

        newnode = Node(ctry_name, init_ctry_code)

        if tree == None:
            self.node = newnode
            self.node.leftChild = AVLTree()
            self.node.rightChild = AVLTree()


        elif ctry_name < tree.ctry_name:
            self.node.leftChild.insert(ctry_name, init_ctry_code)
        elif ctry_name < tree.ctry_name:
            self.node.leftChild.insert(ctry_name, init_ctry_code)
        else: 
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()


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


    def remove(self,ctry_name):
        if self.node != None:
            if self.node.ctry_name
