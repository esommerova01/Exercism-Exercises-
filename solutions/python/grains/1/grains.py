def square(number):
    """Calculate the number of grains on a specific square (1-64)."""
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    """Calculate the total number of grains on the entire chessboard."""
    return (2 ** 64) - 1

    
