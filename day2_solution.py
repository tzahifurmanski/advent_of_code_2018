# Advent of code challenge - day 2
# ================================
from collections import defaultdict


def count_chars_in_word(box_id):
    word_stats = defaultdict(int)

    for char in box_id:
        word_stats[char] += 1

    return word_stats


def is_candidate(box_id_stats):
    found_two = False
    found_three = False

    for _, value in box_id_stats.items():
        if value == 2:
            found_two = True
            continue

        if value == 3:
            found_three = True
            continue

    return (1 if found_two else 0), (1 if found_three else 0)


def compare_words(word1, word2):
    diff = 0
    result_word = word1
    for index in range(len(word1)):
        if word1[index] != word2[index]:
            diff += 1
            result_word = word[0:index] + word[index+1:]

        # Stop soon if words are too different
        if diff > 1:
            return None

    return None if diff == 0 else result_word


box_ids = []

num_of_twos = 0
num_of_threes = 0
candidates = []

file = open("day2_input.txt", "r")
for box_id in file:
    word_stats = count_chars_in_word(box_id)
    twos, threes = is_candidate(word_stats)
    if twos or threes:
        num_of_twos += twos
        num_of_threes += threes
        candidates.append(box_id)
file.close()

# Step 1 - find the result = 6972
print(num_of_twos * num_of_threes)

found = False
for word in candidates:

    for word2 in candidates:
        found_word = compare_words(word, word2)
        if found_word:
            # Step 2 - find the result = aixwcbzrmdvpsjfgllthdyoqe
            print(found_word)
            found = True
            break

    if found:
        break
