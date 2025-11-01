#Braden Phetsarath
#10/28
#Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).
import random

def Random_number_file():
    question1 = int(input("Enter how many numbers do you want generated: "))
    if question1 > 1000:
        print("Number too high. Try a number less than 1000.")
        return
    with open("RND_FILE", "w") as file:
        for i in range(question1):
            number = random.randint(1, 500)
            file.write(str(number)+ "\n")
Random_number_file()
