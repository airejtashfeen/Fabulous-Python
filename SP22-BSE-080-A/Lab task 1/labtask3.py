n_terms = int(input("Enter the number of terms: "))

n1, n2 = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci sequence: {n1}")
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2
        count += 1
