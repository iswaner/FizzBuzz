#Ian Swaner
#08/07/2023
#Fizz Buzz: for numbers 1-100, print the number.
#if the number is a multiple of 3 print Fizz
#if the number is a multiple of 5 print Buzz
#finally if it is a multiple of 3 and 5 print FizzBuzz
#Includes an advanced version where the user can pick the range and the multiples

def fizzBuzz_Classic():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        elif i % 5 == 0:
            print(f"{i} Buzz")
        else:
            print(i)

    return

def advanced(n, a, b):
    for i in range(1, n+1):
        if i % a == 0 and i % b == 0:
            print(f"{i} FizzBuzz")
        elif i % a == 0:
            print(f"{i} Fizz")
        elif i % b == 0:
            print(f"{i} Buzz")
        else:
            print(i)

    return

classic = """FizzBuzz Classic: prints numbers 1 to 100
printing Fizz on multiples of 3, Buzz on multiples
of 5, and FizzBuzz on multiples of both."""

adv = """FizzBuzz advanced: you can pick how
many numbers to list, as well as the 2 multiples to check. """

choice = 0
print("FizzBuzz: Classic or Advanced? \n")
while choice != 1 and choice != 2:
    choice = int(input("1 for classic, 2 for Advanced, 3 for explanation"))

    if choice != 1 and choice != 2:

        print(f"{classic} \n")
        print(f"{adv} \n")


if choice == 1:
    fizzBuzz_Classic()
elif choice == 2:
    n = int(input("How many numbers to check? "))
    a = int(input("Input the first multiple: "))
    b = int(input("Input the second multiple: "))
    advanced(n, a, b)
else:
    sys.exit()
