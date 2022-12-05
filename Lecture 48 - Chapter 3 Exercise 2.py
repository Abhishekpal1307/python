# Lecture 48 - Chapter 3 Exercise 2 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if name[0]=='a' or name[0]=='A' and int(age)>10:
    print("you can watch coco movie")
else:
    print("sorry , you cannot watch coco")