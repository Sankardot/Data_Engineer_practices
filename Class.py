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
#         print(self.childname,"is the son of Mr",self.Fathername,"&",self.Mothername)

# #object creation
# C=Child("Raju","Swamy","Lakshmi")
# C.details()










        
#base class
class Company:
    def __init__(self,Companyname):
        self.Companyname=Companyname
        
class Developer(Company):
    def __init__(self,Developername,designation,Companyname):
        self.Developername=Developername
        self.designation=designation
        super().__init__(Companyname)
    
    def output(self):
        print(self.Developername,"works as",self.designation,"at",self.Companyname)
        
D=Developer("Gowtham","Backend developer","XYZ")
D.output()
        
    
#class tester
class Tester(Company):
    def __init__(self,Testername,designation,Companyname):
        self.Testername=Testername
        self.designation=designation
        super().__init__(Companyname)
    
    def output(self):
        print(self.Testername,"works as",self.designation,"at",self.Companyname)
        
        
T=Tester("Ankith","Devops engineer","XYZ")
T.output()