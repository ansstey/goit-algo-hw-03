import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max<=1000 and min <= quantity >= max:
        result_list = set()
        for result in range(quantity):
            result = random.randint(min, max)
            result_list.add(result)
        return sorted(result_list)
    else:
        return []
        