import random

def main():
    for _ in range(10):  # Repeat 10 times
        value = random.randint(1, 100)  # Random number between 1 and 100
        print(value, end=" ")  # Print on the same line with space

if __name__ == "__main__":
    main()
