def count_letters(file_name):
    counts = {}
    with open(file_name, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Iterate through each character in the line
            for char in line:
                # Check if the character is a letter
                if char.isalpha():
                    # Convert character to lowercase
                    char_lower = char.lower()
                    # Update counts dictionary
                    if char_lower in counts:
                        counts[char_lower] += 1
                    else:
                        counts[char_lower] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # Extract only the letters and convert them to uppercase
    sorted_letters = [item[0].upper() for item in sorted_counts]
    return sorted_letters
file_name = 'input_7_2.txt'
result = count_letters(file_name)
print(result)
