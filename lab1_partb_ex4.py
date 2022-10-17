# A program that finds the sum of numbers from 1 to 1000

"""
def main():
    sum = 0
    n = 1
    
    for number in range (n+1):
        sum = sum + number
    print(sum)    
    
    
main()
#or """

def main():
    num = int(input("Enter the number to calculate from:"))
    sum = 0

    for i in range (1, num+1):
        sum = i + sum

    print("The factorial sum of", num, "is", sum)

main()
    
    
