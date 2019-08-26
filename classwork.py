# # python-functions-cw_2
#
#
# ### Problem 1:
# Create a function that will ask the user for a number. Use the function to get two numbers from the user, then pass the
# two numbers to a function. Add, subtract, multiple, and divide the numbers.

def askUser():
    userInput1 = int(input("Enter a number"))
    userInput2 = int(input("Enter a number"))
    doMath(userInput1, userInput2)
def doMath(number1, number2):
    print(number1 + number2)
    print(number1 - number2)
    print(number1 * number2)
    print(number1 / number2)



def main():
    askUser()
    # doMath()

main()
