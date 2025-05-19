#include <stdio.h>

int main(void)
{
    int rows, cols, i, j, k = 0, temp;
    
    // Accept matrix dimensions
    printf("Enter the number of rows and columns: ");
    scanf("%d %d", &rows, &cols);
    
    int matrix1[rows][cols], matrix2[rows][cols], merged[2 * rows * cols];

    // Accept first matrix
    printf("Enter elements of first matrix: ");
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            scanf("%d", &matrix1[i][j]);

    // Accept second matrix
    printf("Enter elements of second matrix: ");
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            scanf("%d", &matrix2[i][j]);

    // Merge both matrices into a 1D array
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            merged[k++] = matrix1[i][j];

    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            merged[k++] = matrix2[i][j];

    // Bubble sort on merged array
    for (i = 0; i < (2 * rows * cols) - 1; i++)
    {
        for (j = 0; j < (2 * rows * cols) - i - 1; j++)
        {
            if (merged[j] > merged[j + 1])
            {
                temp = merged[j];
                merged[j] = merged[j + 1];
                merged[j + 1] = temp;
            }
        }
    }

    // Print sorted merged matrix
    printf("Sorted Merged Matrix:\n");
    k = 0;
    for (i = 0; i < 2 * rows; i++)
    {
        for (j = 0; j < cols; j++)
            printf("%d ", merged[k++]);
        printf("\n");
    }

    return 0;
}
