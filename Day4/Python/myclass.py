#!/usr/bin/python

class MyClass:
   
      #This is a constructor and gets invoked automaticall
      #When object is created
      def __init__(self):
	  self.x = 0
          self.y = 0

      #This is a member function
      def setValues(self,val1, val2):
	  self.x = val1
          self.y = val2

      #This is a member function
      def printValues(self):
	  print ( 'Value of x : ' + str(self.x) )
	  print ( 'Value of y : ' + str(self.y) )


obj = MyClass()
obj.setValues ( 10, 20 ) # ==> setValues(obj, 10, 20 ) 
obj.printValues( )       # ==> printValues(obj)
