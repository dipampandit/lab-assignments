#include <stdio.h>

#define MAX 10
#define SIZE 20

// Function to get string length
int my_strlen(char str[]) {
    int i = 0;
    while (str[i] != '\0') i++;
    return i;
}

// Function to copy string
void my_strcpy(char dest[], char src[]) {
    int i = 0;
    while ((dest[i] = src[i]) != '\0') i++;
}

// Function to compare strings
int my_strcmp(char a[], char b[]) {
    int i = 0;
    while (a[i] != '\0' && b[i] != '\0') {
        if (a[i] != b[i])
            return 0;
        i++;
    }
    return a[i] == b[i];
}

// Function to sort a string (bubble sort)
void sort_string(char str[]) {
    int i, j, len = my_strlen(str);
    char temp;
    for (i = 0; i < len - 1; i++) {
        for (j = 0; j < len - i - 1; j++) {
            if (str[j] > str[j + 1]) {
                temp = str[j];
                str[j] = str[j + 1];
                str[j + 1] = temp;
            }
        }
    }
}

int main() {
    char words[MAX][SIZE] = {
        "cat", "dog", "tac", "god", "act"
    };
    char sorted[MAX][SIZE];
    int i, j, used[MAX] = {0};

    // Step 1: Make sorted copies
    for (i = 0; i < MAX; i++) {
        my_strcpy(sorted[i], words[i]);
        sort_string(sorted[i]);
    }

    // Step 2: Group by sorted forms
    printf("Grouped Anagrams:\n");
    for (i = 0; i < MAX; i++) {
        if (!used[i]) {
            printf("[ %s", words[i]);
            used[i] = 1;
            for (j = i + 1; j < MAX; j++) {
                if (!used[j] && my_strcmp(sorted[i], sorted[j])) {
                    printf(", %s", words[j]);
                    used[j] = 1;
                }
            }
            printf(" ]\n");
        }
    }

    return 0;
}
