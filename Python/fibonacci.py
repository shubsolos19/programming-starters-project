# Fibonacci Series Generator
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("=== Fibonacci Series Generator ===")
    n = int(input("Enter number of terms: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        result = fibonacci(n)
        print(f"Fibonacci Series ({n} terms): {result}")
        print(f"Sum of series: {sum(result)}")

if __name__ == "__main__":
    main()
