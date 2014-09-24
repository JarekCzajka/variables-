#Jaroslaw Czajka
#24.09.2014
# Spot Check

#This program is about helping the user to calculate the volume of users swimming pool
print("Welcome to the Find the volume of your swimming pool")
print("This program helps the user,to finf the volume of users swimming pool")
#The program has explained to the user,about what the program is about
length=int(input("Please enter the length of your swimming pool:"))
width=int(input("Please enter the width of your swimming pool:"))
depth=int(input("Please enter the depth of your swimming pool:"))
#The program has asked the user for all of the measurment required to calculate the voulume of the swimming pool
volume_of_swimming_pool=(length*width*depth)
print("This is the volume of your swimming pool"),print(volume_of_swimming_pool)
#The program has calculated the main volume of a rectangler shape swimming pool
print("Now we can work out the volume of the  semi-circular shape")
semi_circular_shape=(width/2)
print(semi_circular_shape)
volume_of_semi_circular_shape=(semi_circular_shape*3.14*depth)
print(volume_of_semi_circular_shape)
#The program has calculated the volume of the semi-circular shape
print("Now we can calculate the total volume of the swimming pool")
total_volume=(volume_of_swimming_pool+volume_of_semi_circular_shape)
print(total_volume)
