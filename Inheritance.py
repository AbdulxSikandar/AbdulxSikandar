### Inheritence 

## Inheritance allows us to define a class that inherits all the methods and properties from another class.
## Parent class is the class being inherited from, also called base class.
## Child class is the class that inherits from another class, also called derived class.

## Parent Class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

## Child Class
class Student(Person):
  pass
## Here we are not using __init__() function
## When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
## The child's __init__() function overrides the inheritance of the parent's __init__() function.
## To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

x = Student("Mike", "Olsen")
x.printname()


###############   super() Function #######################

## Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


## By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods 
# # and properties from its parent.

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

## In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects.
##  To do so, add another parameter in the __init__() function:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

## Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)



    # A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Base(object):
     
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
 
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
     
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
 
    # To get name
    def getAge(self):
        return self.age
 
# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
     
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
 
    # To get address
    def getAddress(self):
        return self.address       
 
# Driver code
g = GrandChild("Geek1", 23, "Noida") 
print(g.getName(), g.getAge(), g.getAddress())


## ----------------------  Types of Inheritance in Python ------------------------------------------------------------

##----------Single Inheritance :

##  Single inheritance enables a derived class to inherit properties from a single parent class, 
##  thus enabling code reusability and the addition of new features to existing code.


# Python program to demonstrate
# single inheritance
 
 
# Base class
class Parent:
     def func1(self):
          print("This function is in parent class.")
 
# Derived class
class Child(Parent):
     def func2(self):
          print("This function is in child class.")
 
# Driver's code
object = Child()
object.func1()
object.func2()



##--------------- Multiple Inheritance: 

## When a class can be derived from more than one base class this type 
# of inheritance is called multiple inheritance. In multiple inheritance,
# all the features of the base classes are inherited into the derived class. 


# Python program to demonstrate
# multiple inheritance
 
# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

### Father : RAM
### Mother : SITA





##### Multilevel Inheritance 

## In multilevel inheritance, features of the base class and the derived class are 
# further inherited into the new derived class. This is similar to a relationship
#  representing a child and grandfather. 


# Python program to demonstrate
# multilevel inheritance
 
# Base class
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
 
# Derived class
class Son(Father):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 
#  Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()




### -- Hierarchical Inheritance:
## When more than one derived classes are created from a single base this type 
# of inheritance is called hierarchical inheritance. In this program, we have 
# a parent (base) class and two child (derived) classes.

# Python program to demonstrate
# Hierarchical inheritance
 
 
# Base class
class Parent:
      def func1(self):
          print("This function is in parent class.")
 
# Derived class1
class Child1(Parent):
      def func2(self):
          print("This function is in child 1.")
 
# Derivied class2
class Child2(Parent):
      def func3(self):
          print("This function is in child 2.")
  
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


## Output:
#This function is in parent class.
#This function is in child 1.
#This function is in parent class.
#This function is in child 2.