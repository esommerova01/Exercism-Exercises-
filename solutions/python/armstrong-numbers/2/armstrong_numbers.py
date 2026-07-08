#A function to determine if a number is an armstrong number 
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
    else: 
        return False 

print (is_armstrong_number(153))    
print (is_armstrong_number(154))
