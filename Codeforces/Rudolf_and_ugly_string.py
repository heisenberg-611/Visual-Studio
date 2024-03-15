def min_chars_to_beautiful(s):
    # Initialize counters for "pie" and "map" substrings
    pie_count = 0
    map_count = 0
    
    # Iterate through the string
    for char in s:
        if char == 'p':
            # Check for "pie" substring
            pie_count += 1
        elif char == 'm':
            # Check for "map" substring
            map_count += 1
    
    # Calculate the total characters to remove
    total_chars_to_remove = pie_count + map_count
    
    # Output the result
    return total_chars_to_remove

# Input: Number of test cases
t = int(input())

for _ in range(t):
    # Input: Length of the string and the string itself
    n = int(input())
    s = input().strip()
    
    # Calculate and print the minimum characters to remove
    print(min_chars_to_beautiful(s))
