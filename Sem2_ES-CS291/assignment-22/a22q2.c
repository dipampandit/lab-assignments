#include <stdio.h>

int main() {
    char str[100];
    printf("Enter the string: ");
    scanf("%s", str);

    int i = 0, j = 0;
    int start = 0, maxLength = 0;
    int index[256];

    // Initialize character index map
    for (i = 0; i < 256; i++) {
        index[i] = -1;
    }

    i = 0;
    while (str[i] != '\0') {
        if (index[(unsigned char)str[i]] >= j) {
            j = index[(unsigned char)str[i]] + 1;
        }

        index[(unsigned char)str[i]] = i;

        if (i - j + 1 > maxLength) {
            maxLength = i - j + 1;
            start = j;
        }

        i++;
    }

    printf("Longest substring without repeating characters is: ");
    for (i = start; i < start + maxLength; i++) {
        printf("%c", str[i]);
    }
    printf("\n");

    return 0;
}
