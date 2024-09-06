#Problem5 : Write a program to count the number of zeros in the following tuple

# Program to count the number of zeros in a tuple

def count_zeros(tpl):
    return tpl.count(0)

def main():
    # Define the tuple with some example values
    example_tuple = (0, 1, 2, 0, 3, 4, 0, 5, 0)
    
    # Count the number of zeros
    zero_count = count_zeros(example_tuple)
    
    # Print the result
    print(f"The number of zeros in the tuple is: {zero_count}")

if __name__ == "__main__":
    main()
