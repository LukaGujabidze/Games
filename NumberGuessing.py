import random as r

def run():
    num_guess = r.randint(0, 100)
    times = 0

    while True:
        guesers_in = int(input("Type number from 0 to 100 "))
        if guesers_in > num_guess:
            print('your number is more than secret number')
            times += 1
            
        elif guesers_in < num_guess:
            print('your number is less than secter number')
            times += 1

        elif guesers_in == num_guess:
            print('You win')
            print(times)
            break
        
        else:
            print('you must choose number')    
