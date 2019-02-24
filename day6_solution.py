def print_map(map):
    for row in map:
        row_text = ""
        for col in row:
            row_text += str(col)
        print(row_text)

MATRIX_SIZE = 10

# Initialize the map
coordinates_map = [['.']*MATRIX_SIZE]
for _ in range(10):
    row = list()
    for _2 in range(MATRIX_SIZE):
        row.append('.')
    coordinates_map.append(row)


file = open("day6_input_test.txt", "r")
coordinate_id = 'A'
coordinates = []

for line in file:
    coordinate_details = line.strip().split(", ")
    coordinate = (int(coordinate_details[1]), int(coordinate_details[0]), coordinate_id)
    coordinates.append(coordinate)
    coordinates_map[coordinate[0]][coordinate[1]] = coordinate_id
    coordinate_id = chr(ord(coordinate_id) + 1)
file.close()


def mark_coordinate(coordinate_x, coordinate_y, character, coordinates_map):
    if coordinate_x < 0 or coordinate_x >= MATRIX_SIZE:
        return False

    if coordinate_y < 0 or coordinate_y >= MATRIX_SIZE:
        return False

    current_value = coordinates_map[coordinate_x][coordinate_y]

    # If empty
    if current_value == ".":
        coordinates_map[coordinate_x][coordinate_y] = character.lower()
        return True
    # If already has multiple
    elif current_value == "*":
        return False
    # If it already has a lowercase char
    elif current_value == current_value.lower():
        coordinates_map[coordinate_x][coordinate_y] = "*"
        return True
    # If it's a location, ignore it
    elif current_value == current_value.upper():
        return False
    #if current_value is a character

increment = 1
found_empty_rounds = True
while found_empty_rounds:
    found_empty_rounds = False
    for coordinate in coordinates:
        # Check all coordinates around it
        location_char = coordinate[2]
        # found_empty_rounds |= mark_coordinate(coordinate[0] - increment, coordinate[1] + increment, location_char, coordinates_map)
        found_empty_rounds |= mark_coordinate(coordinate[0] - increment, coordinate[1], location_char, coordinates_map)
        # found_empty_rounds |= mark_coordinate(coordinate[0] - increment, coordinate[1] - increment, location_char, coordinates_map)
        found_empty_rounds |= mark_coordinate(coordinate[0], coordinate[1] - increment, location_char, coordinates_map)
        found_empty_rounds |= mark_coordinate(coordinate[0], coordinate[1] + increment, location_char, coordinates_map)
        # found_empty_rounds |= mark_coordinate(coordinate[0] + increment, coordinate[1] - increment, location_char, coordinates_map)
        found_empty_rounds |= mark_coordinate(coordinate[0] + increment, coordinate[1], location_char, coordinates_map)
        # found_empty_rounds |= mark_coordinate(coordinate[0] + increment, coordinate[1] + increment, location_char, coordinates_map)

    print_map(coordinates_map)
    print()
    print(increment)
    print()
    increment += 1

    # break
print_map(coordinates_map)
