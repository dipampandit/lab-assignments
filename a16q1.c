#include <stdio.h>

int main() {
    int arr[4][4];  // Making space for 1 new column
    int i, j;

    printf("Enter elements for 4x3 matrix:\n");
    for(i = 0; i < 4; i++) {
        for(j = 0; j < 3; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    printf("Enter new column values:\n");
    for(i = 0; i < 4; i++) {
        scanf("%d", &arr[i][3]);  // 4th column
    }

    printf("New 4x4 Matrix:\n");
    for(i = 0; i < 4; i++) {
        for(j = 0; j < 4; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
