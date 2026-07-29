def is_prime(n):
    """
    Returns True if n is a prime number, otherwise False.
    """
    # Numbers less than 2 are NOT prime
    if n < 2:
        return False
    
    # Check if n is divisible by any number from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a divisor, so n is NOT prime
    
    # If no divisors were found, n IS prime
    return True

# Main block - DO NOT CHANGE INDENTATION
if __name__ == "__main__":
    # Get input from user
    num = int(input("Enter a number: "))
    
    # Call the function and store the result
    result = is_prime(num)
    
    # Print the result
    if result:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")