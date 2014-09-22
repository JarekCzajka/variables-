#Jaroslaw Czajka
#22.09.2014
#Class Exercise_Development Exercise_Task2


#This program is about converting units of temperature into metric and imperial units
print("Welcome to UnitConvertor")
print("This program is about helping the user to convert units of temperature")
number_one=int(input("Please enter the the number of degrees in Fahrenheit:"))
#The program has asked the user for the first integer in units
print("This is your temperature in Fahrenheit")
print(number_one)
#The program has displyed the users input
result=(number_one-32*5/9)
print("This is your result in degrees Centigrade")
print(result)
#The program has displyed the result in degrees Centigrade
print("However we can also convert degress Centigrade into Fahrenheit")
number_two=int(input("Please enter the integer of Centigrade:"))
result_two=(number_two+32/5*9)
#The program is now converting the units of degrees Centigrade into Fahrenheit
print("This is your result in degrees Centigrade")
print(result_two)
