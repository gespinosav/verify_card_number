
def verify_number_card(card_number):
       
    digits = [int(n) for n in card_number]
    check_digit = sum(digits[-1::-2] + [sum(divmod(n * 2, 10)) for n in digits[-2::-2]]) % 10 
    
    print('Is {}'.format('valid' if check_digit == 0 else 'invalid'))
    return check_digit == 0
    

if __name__ == "__main__":
    import sys
    verify_number_card(sys.argv[1])

