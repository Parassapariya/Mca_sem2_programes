num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fib_sequence = [0, 1]
    for _ in range(2, num_terms):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    print(f"Fibonacci sequence with {num_terms} terms: {fib_sequence[:num_terms]}")
