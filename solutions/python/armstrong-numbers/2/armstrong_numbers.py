def is_armstrong_number(number):
    digits = len(str(abs(number)))
    armstrong = sum(int(d)**(digits) for d in str(abs(number)))

    return armstrong == number
    

