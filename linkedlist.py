import csv

class Node:
   def __init__(self, init_ctry_name, init_ctry_code):
      self.ctry_name = init_ctry_name
      self.ctry_code = init_ctry_code
      self.ctry_pop = LinkedList()
      self.next = None
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
   def add_ctry_pop(self, new_ctry_pop):
      self.ctry_pop.add(new_ctry_pop)
   def set_next(self, new_next):
      self.next = new_next   
   def print(self)
      print(,end='')

class LinkedList:
   def __init__(self):
      self.head = None
   def is_empty(self):
      return self.head == None
   def add(self, ctry_name, ctry_code):
      temp = Node(ctry_name, ctry_code)
      temp.set_next(self.head)
      self.head = temp     
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
   
   def print_list(self):
      print("PRINTING LINKED LIST")
      currentNode = self.head
      if currentNode == None:
         return 0
      # print(currentNode.get_ctry_name()
      while currentNode != None:
         currentNode = currentNode.get_next()
         if currentNode != None:

            # print(currentNode.get_ctry_name())

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
      if(aux != None):
         contador=1
      while(aux.get_ctry_name() != elem and aux.get_next() != None):
         aux = aux.get_next()
         contador=contador+1
      if(aux.get_ctry_name() == elem):
         print("Found ", elem, "in index", contador)
      else:
         print("The element",elem," could not be found")

   def removeDuplicates(self):
      aux = self.head
      while(aux.get_next() != None):
         if(aux.get_ctry_name() == aux.get_next().get_ctry_name()):
            self.remove(aux.get_ctry_name())
            print("Removed duplicate of",aux.get_ctry_name())
         aux = aux.get_next()



if __name__ == "__main__": 
   l = LinkedList()

   #Ler e inserir os dados
   with open('dados.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
         # print(', '.join(row))
         row=', '.join(row)
         row=row.split(';')
         l.add(row[0],row[1])
         for n in range(0,len(row)):
            break

         #Cada row = Cada país
      l.print_list()


