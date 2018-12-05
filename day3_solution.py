def split_claim(claim):
    claim_details = dict()

    details_array = claim.split(" ")

    claim_details['name'] = details_array[0].lstrip("#")

    location = details_array[2].split(",")
    claim_details['inches_from_left'] = int(location[0])
    claim_details['inches_from_top'] = int(location[1].rstrip(':'))

    size = details_array[3].split("x")
    claim_details['width'] = int(size[0])
    claim_details['height'] = int(size[1].rstrip('\n'))

    return claim_details


size_of_fabric = 1000

# Initialize fabric matrix
fabric = list()
for _ in range(size_of_fabric):
    row = list()
    for _2 in range(size_of_fabric):
        row.append("0")

    fabric.append(row)

# Process claims and put on fabric
claims_list = list()
file = open("day3_input.txt", "r")
for claim in file:
    claim_details = split_claim(claim)
    claims_list.append(claim_details)

    start_col_index = claim_details['inches_from_left']
    start_row_index = claim_details['inches_from_top']

    # Mark the claim on the fabric
    for row_id in range(start_row_index, start_row_index + claim_details['height']):
        for col_id in range(start_col_index, start_col_index + claim_details['width']):
            if fabric[row_id][col_id] == "0":
                fabric[row_id][col_id] = "1"
            else:
                # Cell overlaps with another claim
                fabric[row_id][col_id] = "X"
file.close()


# Go over fabric and count all cells that has X in them
num_of_x = 0
for row in range(size_of_fabric):
    for col in range(size_of_fabric):
        if fabric[row][col] == "X":
            num_of_x += 1

# Step 1 - 110389
print(num_of_x)

# Go over all the claims again and look for the first claim intact
for claim_details in claims_list:
    invalid_claim = False

    start_col_index = claim_details['inches_from_left']
    start_row_index = claim_details['inches_from_top']
    for row_id in range(start_row_index, start_row_index + claim_details['height']):
        for col_id in range(start_col_index, start_col_index + claim_details['width']):
            if fabric[row_id][col_id] != "1":
                invalid_claim = True
                break

        if invalid_claim:
            break

    if not invalid_claim:
        # Step 2 - Answer is 552
        print("Eureka! {}".format(claim_details['name']))
        break
