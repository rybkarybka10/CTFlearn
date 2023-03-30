Card_Number = '543210******1234'

def luhn_algorithm(number):
    length_card = len(number)
    weight = 1
    total = 0
    for i in range(length_card-1, -1, -1):
        if weight == 1:
            total += int(number[i])
            weight = 2
        else:
            product = weight * int(number[i])
            if product > 9:
                product -= 9
            total += product
            weight = 1
    if (total % 10) == 0:
        return True
    else:
        return False

def search_number():
    num1 = '543210' # start card number
    num2 = '1234' # end card number
    for i in range(0, 1000000):
        i = str(i)
        add = 6 - len(i)
        if add != 0:
            i = (add*"0" + i) # length mid number must be ******
            full_number = num1 + i + num2
            if int(full_number) % 123457 == 0 and luhn_algorithm(full_number) == True:
                print(full_number)
        else:
            full_number = num1 + i + num2
            if int(full_number) % 123457 == 0 and luhn_algorithm(full_number) == True:
                print(full_number)

search_number()
