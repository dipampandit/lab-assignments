#include <stdio.h>

// Custom strcmp
int my_strcmp(const char *s1, const char *s2) {
    while (*s1 && (*s1 == *s2)) {
        s1++;
        s2++;
    }
    return *(unsigned char *)s1 - *(unsigned char *)s2;
}

// Custom strcat
void my_strcat(char *dest, const char *src) {
    while (*dest) {
        dest++;
    }
    while (*src) {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}

int main() {
    char str1[100], str2[100], str3[200];

    printf("Enter first string: ");
    scanf("%s", str1);

    printf("Enter second string: ");
    scanf("%s", str2);

    // Compare using custom strcmp
    if (my_strcmp(str1, str2) == 0)
        printf("Strings are equal.\n");
    else
        printf("Strings are not equal.\n");

    // Concatenate using custom strcat
    // First, copy str1 to str3 manually
    int i = 0;
    while (str1[i] != '\0') {
        str3[i] = str1[i];
        i++;
    }
    str3[i] = '\0';

    my_strcat(str3, str2);
    printf("Concatenated string: %s\n", str3);

    return 0;
}
