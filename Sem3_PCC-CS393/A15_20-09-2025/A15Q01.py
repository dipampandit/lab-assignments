import string

Str = """Hello12
            Pen
        How is Going...    !? """

escape_positions = []
word_positions = []
digit_positions = []
punct_positions = []
small_letter_positions = []
capital_letter_positions = []
whitespace_positions = []

for i in range(len(Str) - 1):
    if Str[i] == '\\':   # literal backslash
        escape_positions.append(i)

# Character-by-character checks
for i, ch in enumerate(Str):

    # Digits
    if ch.isdigit():
        digit_positions.append(i)

    # Punctuation
    if ch in string.punctuation:
        punct_positions.append(i)

    # Small letters
    if ch.islower():
        small_letter_positions.append(i)

    # Capital letters
    if ch.isupper():
        capital_letter_positions.append(i)

    # Whitespace
    if ch.isspace():
        whitespace_positions.append(i)


# Word detection (alphanumeric sequences)
words = []
start = None

for i, ch in enumerate(Str):
    if ch.isalnum():
        if start is None:
            start = i
    else:
        if start is not None:
            words.append((Str[start:i], start))
            start = None

if start is not None:
    words.append((Str[start:], start))


# Print results
print("1. Escape Sequences Found At Positions:", escape_positions)
print("2. Total Number of Words:", len(words))
print("   Word Positions:", [pos for word, pos in words])
print("3. Digit Count:", len(digit_positions), "Positions:", digit_positions)
print("4. Punctuation Count:", len(punct_positions), "Positions:", punct_positions)
print("5. Small Letter Count:", len(small_letter_positions), "Positions:", small_letter_positions)
print("6. Capital Letter Count:", len(capital_letter_positions), "Positions:", capital_letter_positions)
print("7. Whitespace Count:", len(whitespace_positions), "Positions:", whitespace_positions)
print("8. Total Length of the String:", len(Str))
