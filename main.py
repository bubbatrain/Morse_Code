
# --------------- 1. LOAD MORSE ALPHABET INTO DICTIONARY

# Dictionary used to store alphabet in txt file
alphabet = {}
# Open txt file, it contains english alphabet and Morse alphabet
with open("alphabet.txt", mode="r") as file:
    # morse_string is used to append corresponding Morse characters
    morse_string = []
    line = file.readline()
    # While there are lines in file, read normal letter and Morse letter
    while line:
        alphabet_letter = line[0]
        morse_letter = line[2::].strip("\n")
        # Populate dict with the alphabet
        alphabet.update(({alphabet_letter:morse_letter}))
        # Continue to read file
        line = file.readline()

# --------------- 2. READ USER MESSAGE AND CONVERT IT TO MORSE

# Loop used to request user input.
valid_input = False
while valid_input == False:
    # Get hold of input message.
    user_string = input("Type your message:\n").replace(" ", "")

    # Validating user input message if it only contains alphanumerical
    # characters. If not, loop iterates again
    if user_string.isalnum():
        valid_input = True

        # Formatting message to all caps lock
        user_string = user_string.upper()
    else:
        print("Please type only letters and numbers.\n")

# For each letter in user_string, append to a list the corresponding
# morse letter
for letter in user_string:
    morse_string.append(f"{alphabet[letter]}  ")
# Formatting morse message as a string
morse_message = "".join(morse_string)

# Display morse message
print(f"\nYour morse message:\n{morse_message}")
