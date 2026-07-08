"""Collatz Conjecture"""
number: int = 1

def steps(number):
    """A function to count the number of steps before an integer reaches 1."""
    if number < 1: 
        raise ValueError("Only positive integers are allowed")

    step_count = 0 

    while number > 1: 
        if number % 2 == 0: 
            number = number // 2
        else: 
            number = number * 3 + 1 
    
        step_count += 1 # Fixed: proper increment operator
    
    return step_count # Fixed: moved outside the loop to return final total
    
FINAL_STEPS = steps(number)
print(f"The number of steps needed to reach 1: {FINAL_STEPS}.") # Fixed: prints the returned value

        
