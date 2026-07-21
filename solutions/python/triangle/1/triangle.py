def triangle_theorem (sides):
    """To see if a triangle meets the conditions."""
    a, b, c = sides 
    return a > 0 and b > 0 and c > 0 \
    and (a + b >= c) and (b + c >= a) and (a + c >= b)


def equilateral(sides):
    """To see if a triangle is an equilateral triangle."""
    a, b, c = sides
    return triangle_theorem(sides)and (a == b == c) 

def isosceles(sides):
    """To see if a triangle is an isosceles triangle."""
    a, b, c = sides 
    if triangle_theorem (sides): 
        return a == b or b == c or c == a 
    return False 
    
def scalene(sides):
    """To see if a triangle is a scalene triangle."""
    a, b, c = sides 
    return triangle_theorem(sides) and (a != b and b != c and a != c)
