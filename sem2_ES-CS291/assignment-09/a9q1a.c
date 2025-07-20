#include <stdio.h>

int main() {
    int i, j, rows = 5;

    for(i = 1; i <= rows; i++) {
        // Print leading spaces
        for(j = 1; j <= rows - i; j++)
            printf(" ");

        // Print stars and spaces in between
        for(j = 1; j <= i; j++) {
            if (j == 1 || j == i || i == rows)
                printf("* ");
            else
                printf("  ");
        }

        printf("\n");
    }

    return 0;
}
