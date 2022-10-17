# A program that inputs 5 numbers from the user in a loop and finds the sum of the numbers.


def main():
# ask the user to input the five numbers
    print("Enter five numbers:")
    
# initilize num to 5 to create a list of 5 numbers
    n = 5
    sum = 0
    
#loop thru numbers entered and find the sum of the inputs   
    for i in range(n):
        number = int(input("Enter number:"))
        sum = number + sum
        
 # output the sum of the five numbers
    print(" The sum of the", n, "numbers is", sum)

main()
        
        
