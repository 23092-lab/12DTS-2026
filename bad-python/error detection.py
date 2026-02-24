choice = 0
def error(choice):
    try:
        choice = int(input())
        print("Your number is....", choice, "!!!\n"""
"""""")
    except ValueError:
        print("Try Again")

while 1:

    print("Enter a number ")
    error(choice)