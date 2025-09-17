import numpy as np
ITALIC = "\033[3m"
BOLD = "\033[1m"
print("WELCOME TO NUMBER GUESSING GAME\n")
random_num=np.random.randint(0,100)

while True:   
    user_num=int(input(BOLD+"GUESS A NUMBER BETWEEN 0 AND 100\n"))
    if user_num==random_num:
        print(ITALIC+"CORRECT GUESS.YOU WON")
        break
    else:
        diff=abs(random_num-user_num)
        if diff<=5:
            print(ITALIC+"SUPER CLOSE.GUESS AGAIN")
        elif diff<=10:
            print(ITALIC+"NOT SUPER CLOSE. YET YOU ARE CLOSE BY")
        elif diff<=20:
            print(ITALIC+"TRY HARDER")
        else:
            print(ITALIC+"WAY TOO FAR AWAY")
        

        if user_num < random_num:
            print(ITALIC+"Hint: Try a HIGHER number.")
        else:
            print(ITALIC+" Hint: Try a LOWER number.")