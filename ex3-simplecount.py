# This program uses both function and then the calling code to 
# call the function again and again with the range of values.

def count_to_n(n):
    for i in range(1, n + 1):
        print(i, end='')
    print()

# Use the input function to get common value for both the 'for' and 'while' loop.
x = int(input("Enter the value of n between 10 to 20: "))

for i in range(1, x):
    count_to_n(i)
n=x
i=0
while n >= i:
    count_to_n(n)
    #print(n-i, end=' ')
    n = n - 1
print()
#-----------------------------------------------------------------------------------------
print("Added this file and code for 3rd commit")
print("Modification for the 4th commit")
