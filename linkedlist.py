import csv

class Node:
   def __init__(self, init_data):
      self.data = init_data
      self.next = None
   def get_data(self):
      return self.data
   def get_next(self):
         return self.next
   def set_data(self, new_data):
      self.data = newdata
   def set_next(self, new_next):
      self.next = new_next   

class LinkedList:
   def __init__(self):
      self.head = None
   def is_empty(self):
      return self.head == None
   def add(self, item):
      temp = Node(item)
      temp.set_next(self.head)
      self.head = temp     
   def remove(self, item):
      current = self.head
      previous = None
      found = False
      while not found:
         if current.get_data() == item:
            found = True      
         else:
            previous = current
            current = current.get_next()
      if previous == None:
         self.head = current.get_next()
      else:
         previous.set_next(current.get_next())  
   
   def print_list(self):
      #print("PRINTING LIST")
      currentNode = self.head
      if currentNode == None:
         return 0
      print(currentNode.get_data())
      while currentNode != None:
         currentNode = currentNode.get_next()
         if currentNode != None:
            print(currentNode.get_data())

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
      while(aux.get_data() != elem and aux.get_next() != None):
         aux = aux.get_next()
         contador=contador+1
      if(aux.get_data() == elem):
         print("Found ", elem, "in index", contador)
      else:
         print("The element",elem," could not be found")

   def removeDuplicates(self):
      aux = self.head
      while(aux.get_next() != None):
         if(aux.get_data() == aux.get_next().get_data()):
            self.remove(aux.get_data())
            print("Removed duplicate of",aux.get_data())
         aux = aux.get_next()



if __name__ == "__main__": 
   l = LinkedList()
   with open('dados.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
         print(', '.join(row))

