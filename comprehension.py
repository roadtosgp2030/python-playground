# LIST COMPREHENSION
# Level 1
square = [i**2 for i in range(1, 11)]
word_lengths = [len(word) for word in ["hello", "world", "python"]]
upper_words = [word.upper() for word in ["hello", "world", "python"]]

# Level 2
divisible_three = [num for num in range(1, 31) if num % 3 == 0]
length_gt_four_words = [
    word for word in ["cat", "elephant", "dog", "tiger", "ant"] if len(word) > 4
]
positive_integers = [num for num in [1, -2, 3, -4, 5, -6] if num > 0]

# Level 3
new_nums = [num if num % 2 == 0 else num * 2 for num in range(1, 7)]
new_words = [
    stripped
    for word in ["  hello  ", "  world  ", "python  ", "tit  "]
    if len(stripped := word.strip()) > 4
]


# DICT COMPREHENSION
# Level 1
square_dict = {num: num**2 for num in range(1, 6)}
word_lengths_dict = {word: len(word) for word in ["apple", "banana", "cherry"]}
keys_values_dict = {key: value for key, value in zip(["a", "b", "c"], [1, 2, 3])}

# Level 2
adult_dict = {
    key: value
    for key, value in {"alice": 25, "bob": 17, "charlie": 30, "dave": 15}.items()
    if value > 18
}
word_length_dict = {
    name: name_length
    for name in ["cat", "elephant", "dog", "tiger"]
    if (name_length := len(name)) > 3
}

# Level 3
reverse_dict = {value: key for key, value in {"a": 1, "b": 2, "c": 3}.items()}
check_dict = {
    name.lower(): "pass" if score >= 80 else "fail"
    for name, score in {"Alice": 85, "Bob": 92, "Charlie": 78}.items()
}


# SET COMPREHENSION
# Level 1
square_set = {num**2 for num in [1, 1, 2, 2, 4, 5, 5, 6]}
first_char_set = {word[0] for word in ["apple", "banana", "cherry", "avocado"]}
double_set = {num * 2 for num in [1, 2, 2, 3, 3, 3, 4]}

# Level 2
odd_set = {num for num in [1, 2, 3, 3, 4, 5, 5, 6, 7, 8] if num % 2 == 1}
gt_four_char_set = {
    word
    for word in ["cat", "elephant", "elephant", "dog", "tiger", "ant"]
    if len(word) >= 4
}

# Level 3
chars_set = {c for c in "hello world" if c != " "}
lower_set = {
    name.lower() for name in ["Alice", "bob", "CHARLIE", "dave", "Dave", "alice"]
}
print(lower_set)
