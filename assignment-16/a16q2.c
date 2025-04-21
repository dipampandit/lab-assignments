#include <stdio.h>

int main() {
    int arr[3][5], i, j, k, l;

    printf("Enter elements for 3x5 matrix:\n");
    for(i = 0; i < 3; i++) {
        for(j = 0; j < 5; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    printf("Duplicate elements:\n");
    for(i = 0; i < 3; i++) {
        for(j = 0; j < 5; j++) {
            for(k = 0; k < 3; k++) {
                for(l = 0; l < 5; l++) {
                    if((i != k || j != l) && arr[i][j] == arr[k][l]) {
                        printf("%d ", arr[i][j]);
                        goto next;
                    }
                }
            }
            next:;
        }
    }

    return 0;
}
