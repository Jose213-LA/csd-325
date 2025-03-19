# Name: Jose Flores
# Date: 3/22/2025
# Assignment: Assignment 1.3
# Purpose: Create a program with the reverse song "100 bottles of beer
#          on the wall."


def countdown_bottles(bottles):
    # Loop to countdown from the number of bottles to 1
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take it down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1

def main():
    # Ask user for input
    try:
        bottles = int(input("Enter number of bottles: "))
        if bottles <= 0:
            print("Please enter a positive number.")
        else:
            countdown_bottles(bottles)
            print("Don't forget to buy more beer!\n")
    except ValueError:
        print("Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()
