from string import ascii_lowercase


def negating_chars(first_char, second_char):
    if first_char == second_char:
        return False
    if str(first_char).lower() != str(second_char).lower():
        return False

    # It's the same char in different polarities
    return True


def is_negating_chars_by_index(input_polymer, first_char_index):
    second_char_index = first_char_index + 1
    if second_char_index >= len(input_polymer):
        return False

    previous_char = input_polymer[first_char_index]
    curr_char = input_polymer[second_char_index]

    return negating_chars(previous_char, curr_char)


def process_polymer(input_polymer):
    output_polymer = ""

    start_index = 0
    for char_index in range(0, len(input_polymer)):
        # Skip iterations that we're already performed
        if char_index < start_index:
            continue

        # Check if adjacent chars are negating, if so skip them and the adjacent chars after them
        characters_removed_after = 0
        while is_negating_chars_by_index(input_polymer, char_index + characters_removed_after):
            characters_removed_after += 2

        if characters_removed_after > 0:
            # Add to the output polymer
            output_polymer += input_polymer[start_index:char_index]

            # Check if there are additional negating chars that we're already processed:
            end_char_index = char_index + characters_removed_after

            # Compare the current char with the last processed char
            while end_char_index < len(input_polymer) and negating_chars(output_polymer[-1:], input_polymer[end_char_index]):
                # Remove the last char since it was negated
                output_polymer = output_polymer[:-1]

                end_char_index += 1

            # Set start index as the next none-negating char
            start_index = end_char_index

    # Append last chars
    output_polymer += input_polymer[start_index:]

    return output_polymer


def get_shortest_polymer(starting_polymer):
    previous_polymer_state = starting_polymer
    curr_polymer_state = process_polymer(previous_polymer_state)
    num_of_executions = 1
    while len(previous_polymer_state) != len(curr_polymer_state):
        previous_polymer_state = curr_polymer_state
        curr_polymer_state = process_polymer(previous_polymer_state)
        num_of_executions += 1
    return curr_polymer_state


# Load the polymer to memory
file = open("day5_input.txt", "r")
base_polymer = file.readline()
file.close()

shortest_polymer = get_shortest_polymer(base_polymer)

# Step 1 - 9116
print(len(shortest_polymer))


# Compute the smallest polymer after removing each chars combination
shortest_polymer_len = len(shortest_polymer)

for char in ascii_lowercase:
    # Create a polymer without the current chars
    curr_polymer = base_polymer.replace(char, "").replace(str(char).capitalize(), "")
    polymer = get_shortest_polymer(curr_polymer)

    if len(polymer) < shortest_polymer_len:
        shortest_polymer_len = len(polymer)

# Step 2 - 6890
print(shortest_polymer_len)
