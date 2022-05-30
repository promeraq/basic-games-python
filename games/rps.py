import random

def main():
    max = int(input("How many times do you wanna play to know the winner?: "))
    result = 0
    for i in range(max):
        user = input("\nChoose between: rock, paper or scissors: ").lower()
        options = ["rock", "paper", "scissors"]
        comp = random.choice(options)
        result = rps(user, comp, result)
        if result > 0:
            print(f"Winning by {result}, {max-i-1} rounds left")
        elif result < 0:
            print(f"Losing by {-result}, {max-i-1} rounds left")
        else:
            print(f"Tied, {max-i-1} rounds left")

    if result > 0:
        print(f"\nNice played! You won by {result}")
    elif result < 0:
        print(f"\nNoobie! You lost by {-result}")
    else:
        print("\nTied")

def rps(user, comp, result):    
    if user == "rock":
        if comp == "rock":
            result += 0
        elif comp == "paper":
            result -= 1
        else:
            result += 1

    elif user == "paper":
        if comp == "rock":
            result += 1
        elif comp == "paper":
            result += 0
        else:
            result -= 1

    elif user == "scissors":
        if comp == "rock":
            result -= 0
        elif comp == "paper":
            result += 1
        else:
            result += 0

    else:
        print("Not valid")
        user = input("rock, paper or scissors: ")
        result = rps(user, comp, result)

    return result

if __name__ == "__main__":
    main()