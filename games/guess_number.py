from random import randint

def guess(number, user_num, max):
    if user_num == number:
        print("You won!!")
        return False
    elif user_num < number and user_num > 1:
        user_num = int(input("Need a bigger number: "))
        guess(number, user_num, max)
    elif user_num > number and user_num < max:
        user_num = int(input("Say a smaller number: "))
        guess(number, user_num, max)
    else:
        user_num = int(input("Out of bounds!!! Say a number again: "))
        guess(number, user_num, max)


def main():
    max = int(input("Max number for game: "))
    number = randint(1, max)
    user_num = int(input(f"Guess the number between 1 and {max}: "))
    play = True
    while play == True:
        play = guess(number, user_num, max)

if __name__ == "__main__":
    main()