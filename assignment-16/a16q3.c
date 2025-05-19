#include <stdio.h>

int main() {
    int arr[3][4], i, j, del_row;

    printf("Enter elements for 3x4 matrix:\n");
    for(i = 0; i < 3; i++) {
        for(j = 0; j < 4; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    printf("Enter row to delete (0 to 2): ");
    scanf("%d", &del_row);

    printf("Matrix after deleting row %d:\n", del_row);
    for(i = 0; i < 3; i++) {
        if(i == del_row)
            continue;
        for(j = 0; j < 4; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
