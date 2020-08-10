import os
import random
magic_number = random.randint(1, 1_000)

os.system("cls")

print("\n\n\n\n\nGuess! how many coconuts this island produced last season?")
print("You can try with 11 numbers")

guess = int(input( "Please, enter a number between 1 and 1.000  :"))

done = False
you_tried = 0

while not done:

    if you_tried >=11:
            print("\n\n\nUpss, Next time maybe you'll guess earlier !!\n\n\n")
            done = True
    
    elif guess < magic_number:
        you_tried += 1
        answer = f"Some more than {guess}"
        print(answer)
        print(f"counter = {you_tried}")
        guess = int(input( "Please, enter a number between 1 and 1.000  :"))
        

    elif guess > magic_number:
        you_tried += 1
        answer = "Too many coconuts !"
        print(answer)
        print(f"counter = {you_tried}")
        guess = int(input( "Please, enter a number between 1 and 1000  :"))
        

    elif guess == magic_number:
        you_tried += 1
        print(f"counter = {you_tried}")
        answer = "\n\n\nthat's right !!!\n\n\n"
        print(answer)
        done = True
        


    