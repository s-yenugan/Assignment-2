a = int(input("Enter a number: "))
if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
sum_number = 0
for i in range(1, 51):
    sum_number += i
print('The sum of integer from range 1 to 50 is: ', sum_number)