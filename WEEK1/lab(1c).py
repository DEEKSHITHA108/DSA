def recursive_search(id_list, target_id, index=0):
    # Base Case 1: Index is out of bounds (ID not found in the list)
    if index >= len(id_list):
        return -1

    # Base Case 2: ID found at the current index
    if id_list[index] == target_id:
        return index

    # Recursive Step: Check the next index
    return recursive_search(id_list, target_id, index + 1)


# Example usage:
employee_ids = [1013, 2045, 3089, 4112, 5067]
target = 3089

# Run the search and print the result
result_index = recursive_search(employee_ids, target)

if result_index != -1:
    print(f"Employee ID {target} found at list index {result_index}.")
else:
    print(f"Employee ID {target} not found in the list.")
