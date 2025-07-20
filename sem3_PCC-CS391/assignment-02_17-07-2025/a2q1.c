#include <stdio.h>

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
            *(C + i * c2 + j) = 0;
            for (int k = 0; k < c1; k++) {
                *(C + i * c2 + j) += (*(A + i * c1 + k)) * (*(B + k * c2 + j));
            }
        }
    }
}

// Display matrix
void displayMatrix(int *M, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", *(M + i * cols + j));
        }
        printf("\n");
    }
}

// Traverse a 1D array using pointer
void traverseArray(int *arr, int n) {
    printf("Traversing 1D array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", *(arr + i));
    }
    printf("\n");
}

// Column-wise search in 2D array
void columnWiseSearch(int *M, int rows, int cols, int key) {
    for (int col = 0; col < cols; col++) {
        for (int row = 0; row < rows; row++) {
            if (*(M + row * cols + col) == key) {
                printf("Element %d found at Row %d, Col %d\n", key, row, col);
                return;
            }
        }
    }
    printf("Element %d not found!\n", key);
}

int main() {
    int r, c;
    printf("Enter rows and cols for matrices: ");
    scanf("%d %d", &r, &c);

    int A[r * c], B[r * c];

    printf("\nEnter elements of Matrix A:\n");
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            scanf("%d", (A + i * c + j));

    printf("\nEnter elements of Matrix B:\n");
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            scanf("%d", (B + i * c + j));

    // Addition
    int C_add[r * c];
    addMatrices(A, B, C_add, r, c);
    printf("\nMatrix A + B:\n");
    displayMatrix(C_add, r, c);

    // Subtraction
    int C_sub[r * c];
    subtractMatrices(A, B, C_sub, r, c);
    printf("\nMatrix A - B:\n");
    displayMatrix(C_sub, r, c);

    // Multiplication
    int C_mul[r * c];
    multiplyMatrices(A, B, C_mul, r, c, c);
    printf("\nMatrix A x B:\n");
    displayMatrix(C_mul, r, c);

    // Traverse a 1D array
    int n;
    printf("\nEnter size of 1D array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter elements: ");
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    traverseArray(arr, n);

    // Column-wise search
    int key;
    printf("\nEnter element to search in Matrix A: ");
    scanf("%d", &key);
    columnWiseSearch(A, r, c, key);

    return 0;
}
