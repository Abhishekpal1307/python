# Lecture 57 - Chapter 3 exercise 4 
num_1= input("Enter more than one digit number: ")
sum_of_digits = 0
i = 0
while i<len(num_1):
    sum_of_digits += int(num_1[i])
    i +=1
print(sum_of_digits)