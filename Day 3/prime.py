def check_prime(numb):
    if(numb < 2):
        return False
    if(numb == 2):
        return True
    i = 2
    prime = True
    while i < numb:
        if((numb % i) == 0):
            prime = False
            break
        i += 1
    return prime


def print_prime(numb1, numb2):
    current_val = numb1
    while current_val <= numb2:
        prime = check_prime(current_val)
        if (prime):
            print(current_val)
        current_val += 1

print_prime(5, 1000000)