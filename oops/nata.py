import random

def GenerateRandom(upper):
    r = random.randint(1, upper)
    return r

def main():
    program = True
    num1 = GenerateRandom(10)
    num2 = GenerateRandom(10)
    result = num1 * num2

    while program:
        ans = input("What is " + str(num1) + "x" + str(num2) + " = ")

        if ans.isdigit():
            if int(ans) == result:
                print("Correct")
                program = False
            else:
                print("Incorrect")
        else:
            print("Answer must be a positive integer")

def new_func():
    x = 10
    for _ in range(x):
        main()

# Call new_func to execute the main function 10 times
new_func()