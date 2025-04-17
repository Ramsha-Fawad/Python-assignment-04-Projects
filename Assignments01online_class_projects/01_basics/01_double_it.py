def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))

    # Keep doubling and printing until curr_value is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == "__main__":
    main()
