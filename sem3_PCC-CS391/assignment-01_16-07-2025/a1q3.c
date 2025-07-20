#include <stdio.h>
#include <stdlib.h>

// Function to add two matrices
void addMatrices(int *A, int *B, int *C, int rows, int cols) {
    for (int i = 0; i < rows * cols; i++) {
        *(C + i) = *(A + i) + *(B + i);
    }
}

// Function to subtract two matrices
void subtractMatrices(int *A, int *B, int *C, int rows, int cols) {
    for (int i = 0; i < rows * cols; i++) {
        *(C + i) = *(A + i) - *(B + i);
    }
}

// Function to multiply two matrices
void multiplyMatrices(int *A, int *B, int *C, int r1, int c1, int c2) {
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            *(C + i * c2 + j) = 0; // initialize
            for (int k = 0; k < c1; k++) {
                *(C + i * c2 + j) += (*(A + i * c1 + k)) * (*(B + k * c2 + j));
            }
        }
    }
}

// Function to display a matrix
void displayMatrix(int *M, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", *(M + i * cols + j));
        }
        printf("\n");
    }
}

int main() {
    int r1, c1, r2, c2;

    printf("Enter rows and cols for Matrix A: ");
    scanf("%d %d", &r1, &c1);

    printf("Enter rows and cols for Matrix B: ");
    scanf("%d %d", &r2, &c2);

    // Allocate memory dynamically
    int *A = (int *)malloc(r1 * c1 * sizeof(int));
    int *B = (int *)malloc(r2 * c2 * sizeof(int));

    printf("\nEnter elements of Matrix A:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            scanf("%d", (A + i * c1 + j));
        }
    }

    printf("\nEnter elements of Matrix B:\n");
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            scanf("%d", (B + i * c2 + j));
        }
    }

    // ADD & SUBTRACT only if same dimensions
    if (r1 == r2 && c1 == c2) {
        int *C_add = (int *)malloc(r1 * c1 * sizeof(int));
        int *C_sub = (int *)malloc(r1 * c1 * sizeof(int));

        addMatrices(A, B, C_add, r1, c1);
        subtractMatrices(A, B, C_sub, r1, c1);

        printf("\nMatrix A + B:\n");
        displayMatrix(C_add, r1, c1);

        printf("\nMatrix A - B:\n");
        displayMatrix(C_sub, r1, c1);

        free(C_add);
        free(C_sub);
    } else {
        printf("\nAddition & Subtraction NOT possible! Matrices must have same dimensions.\n");
    }

    // MULTIPLICATION: possible only if c1 == r2
    if (c1 == r2) {
        int *C_mul = (int *)malloc(r1 * c2 * sizeof(int));
        multiplyMatrices(A, B, C_mul, r1, c1, c2);

        printf("\nMatrix A x B:\n");
        displayMatrix(C_mul, r1, c2);

        free(C_mul);
    } else {
        printf("\nMultiplication NOT possible! (Columns of A must match Rows of B)\n");
    }

    free(A);
    free(B);

    return 0;
}
