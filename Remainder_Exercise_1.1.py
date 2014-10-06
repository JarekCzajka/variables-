#Jaroslaw Czajka
#29.09.2014
#Remainder_Exercise_1.1

#This program is about seeing how many weights weights would balance out the scale
print("Welcome to weight calculator")
weight=int(input("Please enter the weight:"))
hunderd=(weight//100)
print("This is what you get when you take away the hundred")
remainder=weight%100
print(remainder)
fifty=remainder//50
print("This is what you get when you take away the fifty")
remainder=remainder%50
print(remainder)
ten=remainder//10
print("This is what you get when you take away the ten")
remainder=remainder%10
print(remainder)
five=remainder//5
print("This is what you get when you take away the ten")
remainder=remainder%5
print(remainder)
two=remainder//2
print("This is what you get when you take away the two")
remainder=remainder%2
print(remainder)
one=remainder
#The program has carried out all of the tasks

