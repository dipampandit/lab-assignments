#include <stdio.h>

int main(void)
{
    int rows, col;
    printf("Enter the number of rows in the matrix: ");
    scanf("%d", &rows);
    printf("Enter the number of columns in the matrix: ");
    scanf("%d", &col);

    int mat1[rows][col], mat2[rows][col], addMat[rows][col];

    int i, j;
    printf("Enter the Values of the First Matrix:\n");
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("Matrix 1[%d][%d]: ", i, j);
            scanf("%d", &mat1[i][j]);
        }
    }

    printf("Enter the Values of the Second Matrix:\n");
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("Matrix 2[%d][%d]: ", i, j);
            scanf("%d", &mat2[i][j]);
        }
    }

    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < col; j++)
        {
            addMat[i][j] = mat1[i][j] + mat2[i][j];
        }
    }

    printf("The Sum of the Matrices is: \n");
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("%d ", addMat[i][j]);
        }
        printf("\n");
    }
    return 0;
}