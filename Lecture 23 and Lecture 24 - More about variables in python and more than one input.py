#Lecture 23 - More about variables in python
name , age = "harshit" , 24
print("hello"+name+"your age is"+age)
x=y=z=1
print(x+y+z)

#Lecture 24 - Two or more input in one line in python
name = input("enter your name: ")
age = input("enter your age: ")
name , age = input("enter your name and age").split()
print(name)
print(age)