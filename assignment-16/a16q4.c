#include <stdio.h>

int main() {
    int m, n, i, j, zero_count = 0, total;
    printf("Enter matrix size (rows and columns): ");
    scanf("%d %d", &m, &n);
    
    int arr[m][n];
    total = m * n;

    printf("Enter elements of the matrix:\n");
    for(i = 0; i < m; i++) {
        for(j = 0; j < n; j++) {
            scanf("%d", &arr[i][j]);
            if(arr[i][j] == 0)
                zero_count++;
        }
    }

    if(zero_count > total / 2)
        printf("Matrix is Sparse.\n");
    else
        printf("Matrix is Not Sparse.\n");

    return 0;
}
