# Advent of code challenge - day 1
# ================================

# Load the actions to memory
actions_to_perform = []
file = open("day1_input.txt", "r")
for current_action in file:
    actions_to_perform.append(int(current_action))
file.close()

# Initialize frequency related vars
current_frequency = 0
frequencies_history = set()
frequencies_history.add(current_frequency)

found = False
while not found:
    for current_action in actions_to_perform:
        current_frequency += current_action

        # Compare the size of the set before and after I add the current frequency (__len__() is O(1))
        len_before = frequencies_history.__len__()
        frequencies_history.add(current_frequency)
        len_after = frequencies_history.__len__()
        if len_before == len_after:
            # Size is the same, meaning the frequency was seen before
            print("Frequency found! {}".format(current_frequency))
            found = True
            break
