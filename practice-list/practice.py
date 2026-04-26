# ============================================================
# Python List Practice Exercises
# ============================================================
# Instructions: Write your solution under each question.
# Run the file to test your answers.
# ============================================================


# ------------------------------------------------------------
# 1. Sum of a list (Easy)
# Given the list below, print the sum of all elements.
# Do NOT use the built-in sum() function.
# ------------------------------------------------------------
numbers = [3, 7, 2, 9, 4]

# Your code here:
result = 0
for num in numbers:
    result += num
# print(result)

# ------------------------------------------------------------
# 2. Reverse a list (Easy)
# Print the list in reverse order.
# Do NOT use .reverse() or reversed().
# ------------------------------------------------------------
items = [1, 2, 3, 4, 5]

# Your code here:
result = []
length = len(items)
for i in range(length):
    result.append(items[length - 1 - i])
# print(result)

# ------------------------------------------------------------
# 3. Find the largest number (Easy)
# Find and print the largest number in the list.
# Do NOT use max().
# ------------------------------------------------------------
nums = [12, 45, 7, 23, 89, 34]

# Your code here:
if not nums:
    print("Empty list")
else:
    maxNum = float("-inf")
    for num in nums:
        maxNum = num if num > maxNum else maxNum
    # print(maxNum)

# ------------------------------------------------------------
# 4. Remove duplicates (Medium)
# Return and print a new list with duplicates removed.
# Keep the original order.
# ------------------------------------------------------------
data = [1, 2, 2, 3, 4, 4, 4, 5]

# Your code here:
if not data:
    print("Empty list")
else:
    result = []
    seen = set()
    for num in data:
        if num not in seen:
            seen.add(num)
            result.append(num)
    # print(result)
# print(list(dict.fromkeys(data)))


# ------------------------------------------------------------
# 5. Count occurrences (Medium)
# Print how many times each fruit appears in the list.
# ------------------------------------------------------------
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Your code here:
if not data:
    print("Empty list")
else:
    result = {}
    for fruit in fruits:
        if fruit not in result:
            result[fruit] = 1
        else:
            result[fruit] += 1
    # for key, value in result.items():
    #     print(key, value)

# ------------------------------------------------------------
# 6. Flatten a nested list (Medium)
# Combine the inner lists into one flat list and print it.
# Expected: [1, 2, 3, 4, 5, 6]
# ------------------------------------------------------------
nested = [[1, 2], [3, 4], [5, 6]]

# Your code here:
result = []
for item in nested:
    for i in item:
        result.append(i)
# print(result)

# ------------------------------------------------------------
# 7. Rotate a list (Harder)
# Rotate the list to the RIGHT by k steps.
# Expected: [4, 5, 1, 2, 3]
# ------------------------------------------------------------
rotate_nums = [1, 2, 3, 4, 5]
k = 2

# Your code here:
count = 0
while count < k:
    count += 1
    last = rotate_nums.pop()
    rotate_nums.insert(0, last)
print(rotate_nums)

# ------------------------------------------------------------
# 8. Group even and odd (Harder)
# Create two lists -- one with even numbers, one with odd numbers.
# Use a list comprehension for each.
# ------------------------------------------------------------
group_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Your code here:
even = []
odd = []

for num in group_numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
