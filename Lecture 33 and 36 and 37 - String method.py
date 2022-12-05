# Lecture 33 and 36 and 37 and 38 and 39 - String methods till strings are mutable
name = "SaNdaRbh BaJPai"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("a"))

# Lecture 36
name , character = input("enter name and a character comma separated: ").split(",")
print(f"length of your name is : {len(name)}")
print(f"character count : {name.strip().lower().count(character.strip().lower())}")

# Lecture 37
string="She is beautiful and she is a good dancer"
print(string.replace(" ","-"))
print(string.find("is"))
#find positon of is other than 1st
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1 + 1) 
print(is_pos2)

# Lecture 38
name = "Sandarbh"
print(name.center(12, "*"))

name = input("enter your name : ")
print(name.center(len(name)+8, "*"))

# Lecture 39
string="string"
print(string.replace('t','T'))
print(string)