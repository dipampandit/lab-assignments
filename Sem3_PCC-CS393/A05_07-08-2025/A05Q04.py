# Check whether a given alphabet is a vowel or a consonant.
def vowel_or_consonant(ch):
    return "Vowel" if ch.lower() in "aeiou" else "Consonant"

print(vowel_or_consonant("E"))
