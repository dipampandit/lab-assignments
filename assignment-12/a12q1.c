#include <stdio.h>

int main() {
    int i, j, num, temp;

    printf("Enter the number of elements: ");
    scanf("%d", &num);

    int arr[num];

    printf("Enter %d elements: \n", num);
    for (i = 0; i < num; i++) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < num - 1; i++) {
        for (j = 0; j < num - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    printf("Sorted array: ");
    for (i = 0; i < num; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}
