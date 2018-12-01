
# Advent of code challenge - day 1

summarizer = 0
frequencies_history = set()
frequencies_history.add(summarizer)

file = open("input.txt", "r")

found = False
while not found:
    # Open the file and iterate everything
    for line in file:
        summarizer += int(line)

        # Compare the size of the set before and after I add the current frequency
        len_before = frequencies_history.__len__()
        frequencies_history.add(summarizer)
        len_after = frequencies_history.__len__()
        if len_before == len_after:
            # Size is the same, meaning the frequency was seen before
            print("Frequency found! {}".format(summarizer))
            found = True
            break

    # Reset the cursor to the beginning of the file so we can loop again
    file.seek(0, 0)
