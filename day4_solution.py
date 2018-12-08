from datetime import datetime
from collections import defaultdict


def load_actions_log():
    # Load the actions log to memory
    file = open("day4_input.txt", "r")
    log = []
    for log_line in file:
        log.append(log_line)
    file.close()

    # Sort the actions by date (from earliest)
    # TODO: Maybe there's a way to give a function to make it more readable
    log.sort(key=lambda log_entry: datetime.strptime(log_entry.split("] ")[0].lstrip("["), '%Y-%m-%d %H:%M'))
    return log


def map_guard_details(actions_log):
    # Map the actions log to a dict with guard stats
    details = defaultdict(lambda: defaultdict(int))
    current_guard_start_time = None
    current_guard_sleep_minutes = defaultdict(int)

    for entry in actions_log:
        # If this is the first time a guard starts the shirt
        if entry.find("begins shift") > -1:
            # Get new guard and get his current stats
            current_guard_id = entry.split("] ")[1].split(" ")[1].lstrip("#")
            current_guard_sleep_minutes = details[current_guard_id]
        elif entry.find("falls asleep") > -1:
            # Save the sleep start time
            current_guard_start_time = datetime.strptime(entry.split("] ")[0].lstrip("["), '%Y-%m-%d %H:%M').minute
        elif entry.find("wakes up") > -1:
            end_minute = datetime.strptime(entry.split("] ")[0].lstrip("["), '%Y-%m-%d %H:%M').minute - 1

            for curr_min in range(current_guard_start_time, end_minute + 1):
                # Add the minutes from the start to now -1
                current_guard_sleep_minutes[curr_min] += 1

    return details


def find_max(collection):
    max_object = -1
    max_object_value = -1
    for key, value in collection.items():
        if value > max_object_value:
            max_object_value = value
            max_object = key

    return max_object, max_object_value


log = load_actions_log()

guards_details = map_guard_details(log)

# Create a dict with minute stats for step 2
minutes_stats = defaultdict(lambda: defaultdict(int))

# Find the guard with most minutes asleep
max_guard_total_time_asleep = 0
max_guard_id = None
for guard_id, guard_minutes_asleep in guards_details.items():
    guard_total_time_asleep = 0
    for minute, time_asleep_in_minute in guard_minutes_asleep.items():
        guard_total_time_asleep += time_asleep_in_minute

        minutes_stats[minute][guard_id] = time_asleep_in_minute

    if guard_total_time_asleep > max_guard_total_time_asleep:
        max_guard_id = guard_id
        max_guard_total_time_asleep = guard_total_time_asleep


# print("Max guard id: {}, total time asleep {}".format(max_guard_id, max_guard_total_time_asleep))

# Get the minute with most time asleep for the specific guard
max_minute, max_minute_value = find_max(guards_details[max_guard_id])

# print("Max minute where's asleep: {}. Time slept: {}".format(max_minute, max_minute_value))
# Step 1 - 106710
print(int(max_guard_id) * int(max_minute))


top_minutes = dict()
# Find max guard for every minute
for minute, guards in minutes_stats.items():
    max_guard_id, max_guard_value = find_max(guards)

    top_minutes[minute] = {max_guard_id: max_guard_value}


# Find the minute with most time spend

top_minute = None
top_minute_value = -1
top_guard_id = None

for minute, guard in top_minutes.items():
    curr_guard = list(guard.items())[0]
    minute_guard_value = curr_guard[1]
    if minute_guard_value > top_minute_value:
        top_minute_value = minute_guard_value
        top_guard_id = curr_guard[0]

        top_minute = minute

# Step 2 - 10491
print(int(top_minute)*int(top_guard_id))
