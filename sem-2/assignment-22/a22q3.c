#include <stdio.h>

int stringLength(char *str) {
    int len = 0;
    while (str[len] != '\0') len++;
    return len;
}

int isMatch(char *pattern, char *text) {
    // Base cases
    if (*pattern == '\0' && *text == '\0')
        return 1;
    if (*pattern == '*' && *(pattern + 1) == '\0')
        return 1;
    if (*pattern == '*') {
        return isMatch(pattern + 1, text) || (*text && isMatch(pattern, text + 1));
    }
    if (*pattern == '?' || *pattern == *text) {
        return *text && isMatch(pattern + 1, text + 1);
    }
    return 0;
}

int main() {
    char pattern[100], text[100];

    printf("Enter the pattern (use * and ?): ");
    scanf("%s", pattern);
    printf("Enter the text to match: ");
    scanf("%s", text);

    if (isMatch(pattern, text))
        printf("Pattern matches the text!\n");
    else
        printf("Pattern does NOT match the text.\n");

    return 0;
}
