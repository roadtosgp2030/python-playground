import random


get_guess = lambda: random.randint(1, 100)


def play():
    print("Welcome to number guessing game!!!")
    secret = get_guess()
    attempts = 0

    while True:
        attempts += 1
        try:
            num = int(input("Enter guessing number:"))
            if num == secret:
                print(
                    f"You have the correct answer after {attempts} {"attempts" if attempts > 1 else "attempt"}."
                )
                answer = input("Play again? (y/n)")
                if answer == "y":
                    play()
                else:
                    break
            elif num > secret:
                print("Too high!!")
            elif num < secret:
                print("Too low!!")

        except ValueError:
            print("Please enter integer only.")


if __name__ == "__main__":
    play()
