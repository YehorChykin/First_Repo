import random
def get_numbers_ticket(min, max, quantity):
    if (1 <= min <= max <= 1000) and (max-min)>=quantity and quantity>0:
        all_numbers = list(range(min, max+1))
        lottery_numbers=random.sample(all_numbers, quantity)
        return lottery_numbers
    else:
        print(f"Введіть корректні дані")
        return []

lottery_numbers = get_numbers_ticket(1, 35, 5)
print("Ваші лотерейні числа:", lottery_numbers)