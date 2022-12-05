# Lecture 34 - Chapter 2 exercise 3
name , character = input("enter name and a character comma separated: ").split(",")
print(f"length of your name is : {len(name)}")
print(f"character count : {name.lower().count(character.lower())}")