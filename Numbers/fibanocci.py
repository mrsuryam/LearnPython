# fibanocci series 
# 1, 1, 2, 3, 5, 8, 13.. 
# nth term in the series is the sum of n-1 & n-2 term
#Fibonacci Sequence - Enter a number and 
#the program generate the Fibonacci sequence to the Nth number.

first = 1
second = 1

print("Print fibonacci series to the Nth number in series")

number = int(input("Enter the number:"))

for series in range(1, number+1):
    if series == 1:
        print(first, end=" ")
    if series == 2:
        print(first, end=" ")
    if series >=3:
        third = second + first
        print(third, end= " ")
        first=second;
        second=third;

print("")

#Fibonacci Sequence - Enter a number and 
#the program generate the Fibonacci sequence till the given number.

print("Print the Fibonacci series till the given number")

number = int(input("Enter the number:"))

fib=[]
first =1
second=1
third = 0

while third < number:
    if first <= number:
        print(1, end=" ")
    if second<= number:
        print(1, end=" ")
    
    while third < number:
        third = first + second
        fib.append(third)
        first=second
        second =third

for i in fib:
    print(i, end= " ")

print("") 
