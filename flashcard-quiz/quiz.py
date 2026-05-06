import json
import random
from models import Flashcard
from pathlib import Path


def show_score(score: int, total: int) -> None:
    percentage = (score / total) * 100 if total else 0
    print("--------------------------")
    print(f"You got {score} out of {total} correct! {percentage:.2f}%\n")


def implement_question(card: Flashcard) -> bool:
    print(f"Q: {card['question']}")
    user_answer = input("Your answer: ").lower().strip()

    if user_answer == card["answer"]:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The answer was: {card["answer"]}\n")
        return False


def run_quiz(flashcards: list[Flashcard]) -> None:
    if not isinstance(flashcards, list) or len(flashcards) == 0:
        print("Cannot load flashcards...")
        return

    random.shuffle(flashcards)

    score = 0
    total = len(flashcards)
    wrongs: list[int] = []
    is_wrong = False

    for i, card in enumerate(flashcards):
        if implement_question(card):
            score += 1
        else:
            wrongs.append(i)
            is_wrong = True

    show_score(score, total)

    while len(wrongs) > 0:
        is_retry = input(f"You got {len(wrongs)} wrong. Retry them? (y/n): ")
        print("\n")

        if is_retry != "y":
            return

        new_wrongs = []
        for i, wrong in enumerate(wrongs):
            card = flashcards[wrong]
            if implement_question(card):
                score += 1
            else:
                new_wrongs.append(wrong)

        wrongs = new_wrongs

    if is_wrong:
        print("All done!")


if __name__ == "__main__":
    path = Path(__file__).parent + "cards.json"
    with open(path) as f:
        flashcards = json.load(f)
    run_quiz(flashcards)
