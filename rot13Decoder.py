message = input("Please enter a string you want to decode using rot13: ")

# Characters commonly found in flags. We want to skip these because they don't need to be decoded!
skip = "{}_!?"

# Find which characters are uppercase in the cipher text. I use this to keep them uppercase after decoding!
upperIndices = [1 if message[i].upper() == message[i] else 0 for i in range(0, len(message))]

# Make the cipher text all lowercase so we can use the same shift on the numerical ASCII values for each letter
message = message.lower()

# Shift all letters 13 units forward
shifted = [ord(char) + 13 for char in message]
decodedList = []

# If the original, unshifted cipher text is one of our characters to skip, keep it as is. If the ASCII value is greater than '122 (for 'z'), mod by 122 and add 96 (to begin at 'a' again)
for val in shifted:
    if str(chr(val - 13)) in skip:
        decodedList.append(str(chr(val - 13)))
    elif val > 122:
        decodedList.append(str(chr(val % 122 + 96)))
    else:
        decodedList.append(str(chr(val)))

# Transform all originally uppercase letters back to uppercase
decodedList = [decodedList[i].upper() if bool(upperIndices[i]) else decodedList[i] for i in range(len(decodedList))]

print("Decoded with rot13: " + "".join(decodedList))

'''
Note: Below is a failed list comprehension that attempted to do what lines 17-23 (the for loop) accomplishes.

shifted = [ord(char) + 13 if skip.find(char) == -1 else ord(char) for char in message]
decodedList = [str(chr(val)) if (val <= 122 or str(chr(val13)) in skip) else str(chr(val % 122 + 96)) for val in shifted]
'''

