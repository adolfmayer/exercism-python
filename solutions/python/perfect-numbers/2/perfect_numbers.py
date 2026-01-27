def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = []    

    for i in range (1, number):
        if number % i == 0:
            divisors.append(i)

    aliquot_sum = sum(divisors)

    if number > aliquot_sum:
        return "deficient"
    if number < aliquot_sum:
        return "abundant"
    else:
        return "perfect"
