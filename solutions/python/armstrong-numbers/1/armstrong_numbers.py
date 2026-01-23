def is_armstrong_number(number):
    digits = len(str(abs(number)))
    armstrong = sum(int(d)**(digits) for d in str(abs(number)))

    if armstrong == number:
        return (True)
    else:
        return (False)

