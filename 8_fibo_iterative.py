n = int(input("Enter number of terms: "))

#Initial Values a=0, b=1
a, b = 0, 1
step = 0

#this Prints the first two terms of the Fibonacci sequence
print("Fibonacci Sequence:", a, b, end=" ")


for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c
    step += 1


print("\nStep Count (Iterative):", step)
