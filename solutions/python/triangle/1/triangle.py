def equilateral(sides):
    a, b, c = sides
        
    if min(a,b,c) <= 0:
        return False
       
    return a == b == c

def isosceles(sides):
    a, b, c = sides
    
    if min(a,b,c) <= 0:
        return False
    
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return a == b or a == c or b == c   
       
def scalene(sides):
    a, b, c = sides
    
    if min(a,b,c) <= 0:
        return False
    
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return a != b != c != a
