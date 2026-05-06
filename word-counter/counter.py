import string

if __name__ == "__main__":
    print("Welcome to word counter: \n")
    text = input("Enter text: ")

    words = [word.strip(string.punctuation) for word in text.lower().split()]
    words = [w for w in words if w]
    length = len(words)
    unique = len(set(words))

    frequency = {}
    for word in words:
        origin_word = word.strip(string.punctuation)
        frequency[origin_word] = frequency.get(origin_word, 0) + 1

    top5 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:5]
    for word, count in top5:
        print(f"  {word}: {count}")
