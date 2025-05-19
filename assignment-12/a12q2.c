#include <stdio.h>

int main() {
    int rows, cols, i, j, k, temp;

    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printf("Enter the number of columns: ");
    scanf("%d", &cols);

    int arr[rows][cols];

    printf("Enter the elements of the table (%d x %d):\n", rows, cols); 
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols - 1; j++) {
            for (k = 0; k < cols - j - 1; k++) {
                if (arr[i][k] > arr[i][k + 1]) {
                    temp = arr[i][k];
                    arr[i][k] = arr[i][k + 1];
                    arr[i][k + 1] = temp;
                }
            }
        }
    }

    printf("\nSorted table (row-wise):\n");
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
