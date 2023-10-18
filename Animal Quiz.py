import time
# Set start score to 0
score = 0

# The function which check answer correctness
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer")
            score = score + 3 - attempt
            still_guessing = False         
        else:
            if attempt < 2:
                guess = input("Wrong answer, try again ")
            attempt = attempt + 1    
            
    if attempt == 3:
        print('Correct answer is ' + answer)

  
print("Guess the Animal!")

# Qeustions section
guess1 = input('which bear lives at the North Pole?\n \
A) Penguin\n B) Seal\n C) Bear\n D) Polar bear\n \
Type A, B, C or D\n')
check_guess(guess1, "D")

guess2 = input('which lizard was the largest? \n \
A) Crocodile\n B) Lizard\n C) Dinosaur\n D) fish\s \
Type A, B, C, D\n')   
check_guess(guess2, "C")

guess3 = input('which is the fastest land animal?\n \
A) Leopard\n B) Cheetah\n C) Bear\n D) Shark\n \
Type A, B, C or D\n')
check_guess(guess3, "B")

guess4 = input('which is largest animal? \n \
A) Elephant\n B) Rhinoceros\n C) Blue Whale\n D) Giraffe\n \
Type A, B, C or D\n')    
check_guess(guess4, "C")

# Print final score
print('your score is ' + str(score) + ' / 12')

time.sleep(5)
