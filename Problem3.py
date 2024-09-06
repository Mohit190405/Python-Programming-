#Problem3: Check that a tuple type cannot be changed in python
# Program to demonstrate the immutability of tuples

def demonstrate_tuple_immutability():
    # Create a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("Original tuple:", my_tuple)
    
    try:
        # Attempt to change an element in the tuple
        my_tuple[2] = 99
    except TypeError as e:
        print("Error:", e)
    
    # Print the tuple to confirm it hasn't changed
    print("Tuple after attempted modification:", my_tuple)

def main():
    demonstrate_tuple_immutability()

if __name__ == "__main__":
    main()
