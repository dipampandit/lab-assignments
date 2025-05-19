#include <stdio.h>

int main(void)
{
    int rows, col;
    printf("Enter the number of rows in the matrix: ");
    scanf("%d", &rows);
    printf("Enter the number of columns in the matrix: ");
    scanf("%d", &col);

    int mat[rows][col];

    int i, j;
    printf("Enter the Values of the Matrix:\n");
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("Matrix[%d][%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }

    int max = mat[0][0];
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < col; j++)
        {
            if(mat[i][j] > max)
                max = mat[i][j];
        }
    }
    printf("Maximum value from the matrix: %d\n", max);

    return 0;
}