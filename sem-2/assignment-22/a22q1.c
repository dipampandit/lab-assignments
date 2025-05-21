#include <stdio.h>

int main() {
    char ch;
    int vowels = 0, consonants = 0, digits = 0, special = 0;
    int uppercase = 0, lowercase = 0;
    int tabs = 0, spaces = 0, newlines = 0;

    printf("Enter text :\n");
    
    while ((ch = getchar()) != EOF) {
        if ((ch >= 'A') && (ch <= 'Z')) {
            uppercase++;
            ch = ch + 32; // convert to lowercase for vowel/consonant check
        } else if ((ch >= 'a') && (ch <= 'z')) {
            lowercase++;
        }

        if ((ch >= 'a') && (ch <= 'z')) {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                vowels++;
            else
                consonants++;
        } else if (ch >= '0' && ch <= '9') {
            digits++;
        } else if (ch == ' ') {
            spaces++;
        } else if (ch == '\t') {
            tabs++;
        } else if (ch == '\n') {
            newlines++;
        } else {
            special++;
        }
    }

    printf("Vowels: %d\nConsonants: %d\nDigits: %d\nSpecial: %d\n", vowels, consonants, digits, special);
    printf("Uppercase: %d\nLowercase: %d\nTabs: %d\nSpaces: %d\nNewlines: %d\n", uppercase, lowercase, tabs, spaces, newlines);

    return 0;
}
