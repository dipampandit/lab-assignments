#include <stdio.h>

void printMarks(int marks[3][4]) {
    for (int i = 0; i < 3; i++) {
        printf("Student %d: ", i + 1);
        for (int j = 0; j < 4; j++) {
            printf("%d ", marks[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int marks[3][4] = {
        {85, 90, 95, 80},
        {78, 88, 84, 90},
        {92, 76, 85, 89}
    };
    printMarks(marks);
    return 0;
}
