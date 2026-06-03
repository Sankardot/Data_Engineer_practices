# def is_anagram(a, b):

#     if len(a) != len(b):
#         return "Not Anagram"

#     if sorted(a) == sorted(b):
#         return "Anagram"
#     else:
#         return "Not Anagram"

# print(is_anagram("race", "care"))






# s1, s2 = "listen", "silent"; print(sorted(s1.care()) == sorted(s2.race()))








# class Car:

#     def __init__(self, brand, model, color, price):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.price = price

#     def details(self):
#         return f"""
# Brand : {self.brand}
# Model : {self.model}
# Color : {self.color}
# Price : {self.price}
# """


# car1 = Car("BMW", "X5", "Black", "90 Lakhs")

# print(car1.details())




# class Student: #class creation
#     college_name="Amara college";
#     #default
#     def __init__(self):
#         pass
#     #parameterised
#     def __init__(self,fname,location):
#         self.name=fname
#         self.location=location
#         pass
    
# #Object_name=classname(attributes1,........)
# S1=Student("Ankith","Bangalore")
# print(S1.name,S1.location)
# print(S1.college_name)
# print(Student.college_name)





   
# class Animal:
#     bread="PUG"
#     def __init__(self,name):
#         self.name=name
    

# class Dog(Animal):
#     bread="germanshephord"
#     def sound(self):
#         print(self.name,"barck")
# d=Dog("Chintu")
# print(d.bread)
# d.sound()

# class Cat(Animal):
#     def sound(self, msg):
#         print(self.name, "meow", msg)
# c=Cat("Catty")
# c.sound("he")
# print(c.bread)








#Single level inheritance

# class Vehicle:
#     def __init__(self,name):
#         self.name=name
        
# class Bike(Vehicle):
#     def speed(self):
#         print(self.name,"120km")
        
# #object creation
# b=Bike("Ns200")
# b.speed()










# #Base class
# class Organization:                                                         #Created a A class 
#     def __init__(self,Organizationname):
#         self.Organizationname=Organizationname
        
# class Company(Organization):
#     def __init__(self,Companyname,Organizationname):                        #created a B class
#         self.Companyname=Companyname
#         #self.Organizationname=Organizationname
#         Organization.__init__(self,Organizationname)
    
# class Product(Company):
#     def __init__(self,Productname,Companyname,Organizationname):
#         self.Productname=Productname
#         #calling the constructor of Company
#         Company.__init__(self,Companyname,Organizationname)                 #Created a C class
#     def details(self):
#         print("Organization name:",self.Organizationname)
#         print("Company name :",self.Companyname)
#         print("Product name :",self.Productname)
        
    
# #object creation
# P=Product("Altroz","TataMotors","TATA")
# P.details()


# #Base class 1
# class Father:
#     def __init__(self,Fathername):
#         self.Fathername=Fathername

# #Base class 2
# class Mother:
#     def __init__(self,Mothername):
#         self.Mothername=Mothername
        
# #derived class/child class
# class Child(Father,Mother):
#     def __init__(self,childname,Fathername,Mothername):
#         self.childname=childname
#         Father.__init__(self,Fathername)
#         Mother.__init__(self,Mothername)
        
#     def details(self):
# #         print(self.childname,"is the son of Mr",self.Fathername,"&",self.Mothername)

# # #object creation
# # C=Child("Raju","Swamy","Lakshmi")
# # C.details()










        
# #base class
# class Company:
#     def __init__(self,Companyname):
#         self.Companyname=Companyname
        
# class Developer(Company):
#     def __init__(self,Developername,designation,Companyname):
#         self.Developername=Developername
#         self.designation=designation
#         super().__init__(Companyname)
    
#     def output(self):
#         print(self.Developername,"works as",self.designation,"at",self.Companyname)
        
# D=Developer("Gowtham","Backend developer","XYZ")
# D.output()
        
    
# #class tester
# class Tester(Company):
#     def __init__(self,Testername,designation,Companyname):
#         self.Testername=Testername
#         self.designation=designation
#         super().__init__(Companyname)
    
#     def output(self):
#         print(self.Testername,"works as",self.designation,"at",self.Companyname)
        
        
# T=Tester("Ankith","Devops engineer","XYZ")
# T.output()





# method overlaoding : same name and  different parameters 
# it is assocaited with compile type polymorphism 


# class demo():
#     def add(a,b):
#         print(sum(a,b))
        
#     def add(a, b, c):
#         print(sum(a, b, c))
# d = demo()
# d.add(1,2)
# d.add(1,2,3)

#  it is will throw error because python does not support method overlaoding but we can achieve method overloading 
#  by using default parameters or variable length arguments

# * Args : it is used to pass a variable number of non keyword arguments to a function

# class demo():
#     def add(self, *a):
#         print(sum(a))
#     def add(self, *a):
#         print(sum(a))
# d = demo()
# d.add(1,2)
# d.add(1,2,3,2,32)



# runtime : it is associated with polymorphism and it is achieved by method overridding
#  it is dynamic binding 
#  it is called as method overridding 
  
# method overridding : same name and same paramters  in parent class and child class


# class animal:
#     def sound(self):
#         print("animal makes sound")

# class dog(animal):

#     def sound(self):
#         print("Dog barks")
# obj = dog()
# obj.sound()

# it will print child class method because it is overridding  the parenent class

# superkeyword() it is used to call a method from the parent class in tha child class




# class animal:
#     def sound(self):
#         print("animal makes sound")
        
# class dog(animal):
#     def sound(self):
#         super().sound() # it will call the parent class method
#         print("Dog barks")
        
        
# obj = dog()
# obj.sound()




# it will print both because we are using the super keyword to call the aprenet class in the child class method






# encapsulation: wrapping a data and methods into a single logical unit is called encapsulation 

# they are acces modifers : public, protected , private 


# it is used to protect data from the unauthrized access and modification 


# public : is is accessible from any where  in the program 

# class public:
#     def __init__(self,name):
#         self.name= name 
    
#     def output(self):
#         print("my name is", self.name)
# p = public("sanki")
# p.output() 



# this is called punblic beacause we can access the data and method from any where in the program 



# protected: it is accessible with in the class and its subclasses but not out side  the class 

# class protected:
#     def __init__(self,name, age):
#         self.name = name
#         self._age = age
#     def display(self):
#         print("my name is", self.name)
# class sub(protected):
#     def output(self):
#         print("my age is", self._age)
# p = sub("Sanki", 23)
# p.display()
# p.output()



# private : it is accesible only within the class and not outside the class

# class private:
    
#     def __init__(self,name,age, salary):
#         self.name = name 
#         self._age = age 
#         self.__salary = salary
#     def display(self):
#         print("my name is", self.name)
#         print("my age is", self._age)
#         print("my salary is", self.__salary)
# p = private("sanki", 23, 34323)
# p.display()




# local varible : a varible id define dinside the function is called a local variable 
# it can be only accesed inside the function 
# it is created when the function starts and destroyed when the fucntion ends 



# def my_function():
#     x = 10 
#     print("inside the function", x)
# my_function()






# global variable : a variable s defined outside the fucntion is called a global variable 
# it can be acceed from any where in the program 

#  but if u want modify inisde the fucntion you must use the global keyword to modify
# the global varible inside the fucntion 
 
 
 
# y = 20 
# def mu_function():
#     global y
#     y =  30 
#     print("inside the function", y)
# mu_function()
# print("outside the function", y)