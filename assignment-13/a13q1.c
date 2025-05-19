#include <stdio.h>

int main() {
    int i, j, rows, cols;
    
    printf("Enter number of rows and columns: ");
    scanf("%d %d", &rows, &cols);
    
    int arr[rows][cols];

    printf("Enter elements of the matrix:\n");
    for(i = 0; i < rows; i++)
        for(j = 0; j < cols; j++)
            scanf("%d", &arr[i][j]);

    // Finding maximum in each row
    printf("Maximum in each row:\n");
    for(i = 0; i < rows; i++) {
        int maxRow = arr[i][0];
        for(j = 1; j < cols; j++) {
            if(arr[i][j] > maxRow)
                maxRow = arr[i][j];
        }
        printf("Row %d: %d\n", i + 1, maxRow);
    }

    // Finding maximum in each column
    printf("Maximum in each column:\n");
    for(j = 0; j < cols; j++) {
        int maxCol = arr[0][j];
        for(i = 1; i < rows; i++) {
            if(arr[i][j] > maxCol)
                maxCol = arr[i][j];
        }
        printf("Column %d: %d\n", j + 1, maxCol);
    }

    return 0;
}
