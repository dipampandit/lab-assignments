#include <stdio.h>

int main() {
    int i, j, k, rows, cols, temp;
    
    printf("Enter number of rows and columns: ");
    scanf("%d %d", &rows, &cols);
    
    int arr[rows][cols];

    printf("Enter elements of the matrix:\n");
    for(i = 0; i < rows; i++)
        for(j = 0; j < cols; j++)
            scanf("%d", &arr[i][j]);

    // Row-wise Bubble Sort
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols - 1; j++) {
            for(k = 0; k < cols - j - 1; k++) {
                if(arr[i][k] > arr[i][k + 1]) {
                    temp = arr[i][k];
                    arr[i][k] = arr[i][k + 1];
                    arr[i][k + 1] = temp;
                }
            }
        }
    }

    // Display sorted matrix
    printf("Row-wise sorted matrix:\n");
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++)
            printf("%d ", arr[i][j]);
        printf("\n");
    }

    return 0;
}
