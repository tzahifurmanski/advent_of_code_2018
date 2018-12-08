from string import ascii_lowercase


def is_negating_char(input_polymer, char_index, end_index=None):
    if char_index >= len(input_polymer):
        return False

    previous_char = input_polymer[char_index - 1]
    curr_char = input_polymer[char_index]

    if previous_char == curr_char:
        return False
    if str(previous_char).lower() != str(curr_char).lower():
        return False

    # It's the same char in different polarities
    return True


def process_polymer(input_polymer):
    output_polymer = ""

    # previous_char = ''
    start_index = 0
    for char_index in range(1, len(input_polymer)):
        # Skip iterations that we're already performed
        if char_index <= start_index:
            continue

        after_removal_range = 0

        while is_negating_char(input_polymer, char_index + after_removal_range):
            after_removal_range += 2

        if after_removal_range > 0:
            # TODO: Check if there are additional negating chars before

            # Remove from the previous start index until current position
            output_polymer += input_polymer[start_index:char_index-1]

            # Set start index as the next none negating char
            start_index = char_index + after_removal_range - 1

        # if is_negating_char(input_polymer, char_index):
        #     after_removal_range = 2
        #
        #     # Check if there are additional negating chars after
        #     while is_negating_char(input_polymer, char_index + after_removal_range):
        #         after_removal_range += 2
        #
        #     # Check if there are additional negating chars before
        #
        #     # Add everything up until the previous char
        #     output_polymer += input_polymer[start_index:char_index-1]
        #
        #     # Next not negating char + skip what we've currently tested
        #     start_index = char_index + after_removal_range - 1

    # Append last chars
    output_polymer += input_polymer[start_index:]

    return output_polymer


def get_shortest_polymer(base_polymer):
    previous_polymer = base_polymer
    curr_polymer = process_polymer(previous_polymer)
    while len(previous_polymer) != len(curr_polymer):
        # print(len(previous_polymer), len(curr_polymer))
        previous_polymer = curr_polymer
        curr_polymer = process_polymer(previous_polymer)

    return curr_polymer


# Load the polymer to memory
file = open("day5_input.txt", "r")
base_polymer = file.readline()
file.close()

shortest_polymer = get_shortest_polymer(base_polymer)

# Step 1 - 9116
print("Done Basic - {}".format(len(shortest_polymer)))


# Compute the best polymer after removing each chars combination
# shortest_polymer_len = -1
#
# for char in ascii_lowercase:
#     # Create a polymer without the current chars
#     curr_polymer = base_polymer.replace(char, "").replace(str(char).capitalize(),"")
#     polymer = get_shortest_polymer(curr_polymer)
#
#     if len(polymer) > shortest_polymer_len:
#         shortest_polymer_len = len(polymer)
#
# print(shortest_polymer_len)
