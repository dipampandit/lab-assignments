#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100], str3[200];

    // Input strings
    printf("Enter first string: ");
    scanf("%s", str1);

    printf("Enter second string: ");
    scanf("%s", str2);

    // String comparison
    if (strcmp(str1, str2) == 0)
        printf("Strings are equal.\n");
    else
        printf("Strings are not equal.\n");

    // String concatenation
    strcpy(str3, str1);     // Copy str1 to str3 first
    strcat(str3, str2);     // Concatenate str2 to str3
    printf("Concatenated string: %s\n", str3);

    return 0;
}
