

# 1. Check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# 2. Find largest of three numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 3. Print numbers from 1 to 10 using loop
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")


# 4. Sum of first N numbers
n = int(input("\n\nEnter value of N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "numbers is:", total)


# 5. Multiplication table
num = int(input("\nEnter number for multiplication table: "))

print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
