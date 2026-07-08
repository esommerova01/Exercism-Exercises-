"""Module provides a function to determine if a number is an armstrong number or not."""

def is_armstrong_number(number):
    """Function to determine if a number is an armstrong number"""
    text = str(number)
    power = len(text)

    total = 0 
    for character in text: 
        digit = int(character)
        total += digit ** power 

    if total == number: 
        return True
    if total != number:  
        return False

print (is_armstrong_number(153))    
print (is_armstrong_number(154))
