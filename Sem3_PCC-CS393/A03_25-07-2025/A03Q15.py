ch = input("Enter a character: ")
if ch.isalpha():
    print("Vowel" if ch.lower() in 'aeiou' else "Consonant")
else:
    print("Not an alphabet")
