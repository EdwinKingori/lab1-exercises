# Finding the sum and average of five numbers entered as input
import math

def main():
    print("Enter Five Numbers")

    num = 5
    sum = 0

    for i in range(num):
        number = int(input("Enter Number:"))
        sum = number + sum
       
    print("The sum of the", num, "numbers is", sum)
    average = sum / num
    print ("The average of the", num, "numbers is", average) 
        
main()
