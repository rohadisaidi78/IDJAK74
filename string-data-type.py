#String Data Type
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
#String Concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
#Working with input String
name = input("What is your name? ")
print(name)
#Formatting output strings
warna = input("Apa warna kesukaan Anda? ")
hewan = input("Apa hewan kesukaan Anda? ")
print("{}, Anda menyukai {} {}!".format(name,hewan,warna))
