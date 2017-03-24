class PopNode:
   def __init__(self, newyear, newpop):
      self.year = newyear
      self.percentpop = newpop
      # self.ctry_name = init_ctry_name
      # self.ctry_code = init_ctry_code
      # self.ctry_pop = {}
      # for i in range(0,57):
      #    self.ctry_pop[1960+i] = ''
      self.next = None
   def get_pop(self):
      return self.percentpop
   def get_year(self):
      return self.year
   def get_next(self):
      return self.next
   def set_pop(self, newinfo):
      self.percentpop = newinfo
   def set_year(self, newinfo):
      self.year = newinfo
   def set_next(self, new_next):
      self.next = new_next
   def nodeprint(self):
       print(self.newyear,self.percentpop)


class AuxiliarLinkedList:
   def __init__(self):
      self.head = None
      for x in range(0,57):
         self.add(2016-x,'')

   def is_empty(self):
      return self.head == None

   def add(self, newyear, newpercent):
      temp = PopNode(year, newpercent)
      temp.set_next(self.head)
      self.head = temp
      return self.head

   def remove(self, item):
      current = self.head
      previous = None
      found = False
      while not found:
         if current.get_info() == item:
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

# Find: Inserir ano e ele retorna o nó com esse ano
   def find(self, elem):
      aux = self.head
      while(aux.get_year() != elem and aux.get_next() != None):
         aux = aux.get_next()
      if(aux.get_year() == elem):
         print("Encontrou o ano", elem)
         return aux
      else:
         print("O ano",elem,"não foi encontrado")
         return None

   def removeDuplicates(self):
      aux = self.head
      while(aux.get_next() != None):
         if(aux.get_info() == aux.get_next().get_info()):
            self.remove(aux.get_info())
            print("Removed duplicate of",aux.get_info())
         aux = aux.get_next()