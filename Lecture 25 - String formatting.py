#Lecture 25 - String formatting
#nomral way 
name = "harshit"
age = 24
print("hello"+name+"your age is"+str(age)) #ugly syntax
# using string formatting
print("hello {} your age is {}".format(name,age))
#3.6
print(f"hello {name} your age is {age}") #clean