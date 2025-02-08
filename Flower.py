#Allison Vasarab 2-8-2025
#The purpose of this code is to make a class with objects that have methods with outputs, with an added object of my own

class Flower: #This is defining the class Flower
    def __init__(self, name): #Assigns values to object properties
        self.name = name #Constructor menthod to assign name to objects attributes

    def grow(self): #The def method for grow
        print("The " +self.name + " is growing.") #An output for an object and method

    def bloom(self): #The def method for bloom
        print("The " +self.name + " is blooming.") #An output for an object and method

def main(): #Defining main function 
    flower1 = Flower("Rose") #Making a flower object called rose, an instance of flower
    flower1.grow()  #Giving the object a method of grow
    flower1.bloom() #Giving the object another method of bloom
    flower2 = Flower("Daisy") #Making a flower object called Daisy, an instance of flower
    flower2.grow()  #Giving the second object a method of grow with a dot operator
    flower2.bloom() #Giving the second object a method of bloom with a dot operator
    flower3 = Flower("Sunflower")   #Making a flower object called sunflower, an instance of flower
    flower3.grow()  #Giving the object a method of of grow
    flower3.bloom() #Giving the object another method of grow
    
if __name__ == "__main__": #calls main function and runs it
  main() #function being called