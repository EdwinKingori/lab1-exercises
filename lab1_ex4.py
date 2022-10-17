#Two Methods of Finding the squareroot of a number
#importing from math module

import math

def main():
    num = int(input("Enter a number:"))
    result = math.sqrt(num) or
    print("The squareroot of", num, "is", result)

main()

# or

# without importing from math module

def main():
    num = int(input("Enter a number:"))
    result = num **0.5
    print("The squareroot of", num, "is", result)

main()
    
