def is_valid(isbn):
    isbn = [char for char in isbn if char.isalnum()]

    if len(isbn) != 10:
        return False
    
    result = 0
    multi  = 10

    for char in isbn:

        if char.isalpha() and char != "X":
            return False
        
        if char == 'X':
            if multi == 1:
                val = 10
            else:
                return False
                
        else:
            val = int(char)

        result += val * multi
        multi -= 1
    
    return result % 11 == 0
        