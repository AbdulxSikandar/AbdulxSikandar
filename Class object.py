## -------------------------- Class ------------------------------------

## CLASS - Class is a blue print for a object which we are going to create
          #A Class is like an object constructor, or a "blueprint" for creating objects.






### -------------------------------------------------------------------------------------------------------------------------------------

class Student :
    Class ='10th'                              ### Class Attributes
    School = 'St. Wilfird School'


    def __init__(self,name,city) -> None:              ## Constructor / a special method which runs as soon as object created
        self.Name = name                 #### Object Attributes
        self.City = city

    def studentDetails(self):                ## method
        return f"Name = {self.Name} ,City = {self.City},Class = {self.Class} ,School = {self.School}"


student1 = Student('Deepak','Delhi')                        ## Calling a class
print(student1.studentDetails())           


student2 = Student('Faisal','Jaipur')
student2.City = 'Sikar'                     ## Modification or Updation of object attribute
student2.Class = '11th'                     ## Modification or Updation of class attribute
print(student2.studentDetails())



### ---------------- STATIC METHOD -------------------------------

## a method which is not having any parameter is callable only by class
## static method knows nothiing about the class and just deals with the parameters
## @staticmethod is must to write before method

@staticmethod
def person():
    print( "Welcome to Earth" )


### -------------------------------------------------------------------------------------------------------------------------------------
