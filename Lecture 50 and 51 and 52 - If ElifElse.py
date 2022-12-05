# Lecture 50 and 51 and 52 - If ElifElse statement and keywords and empty or not
age = int(input("Please input your age: "))
if age==0:
    print("You cannot watch")

if 0<age<=3:
    print("Ticket price : Free")
elif 3<age<=10:
    print("Ticket Price; 150")
elif 10<age<=600:
    print("Ticket Price : 250")
else:
    print("Ticket Price : 200")

# Lecture 51
name = "Sandarbh"
if 'a' in name:
    print("a is present in name")
else:
    print("not present")

# Lecture 52
name = input("enter your name: ")
if name: 
    print(f"your name is {name}")
else:
    print("you did not type anything")