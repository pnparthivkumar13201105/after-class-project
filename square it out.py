def square_and_filter(start, end):
    
    squares = [x**2 for x in range(start, end + 1)]

    odd_squares = [num for num in squares if num % 2 != 0]
    even_squares = [num for num in squares if num % 2 == 0]
    
    print("Squares:", squares)
    print("Odd Squares:", odd_squares)
    print("Even Squares:", even_squares)

square_and_filter(1, 10)
