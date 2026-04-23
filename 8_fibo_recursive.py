step = 0  # global step counter

#₹ Recursive Fibonacci function
def fibonacci(n):
    global step
    if n <= 1:
        return n
    
    step += 1  # count each recursive expansion
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter number of terms: "))

print("Fibonacci Sequence:", end=" ")

for i in range(n):
    print(fibonacci(i), end=" ")

print("\nStep Count (Recursive):", step)
