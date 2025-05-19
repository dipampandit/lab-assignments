#include <stdio.h>

int main() {
    int arr[] = {23, 11, 45, 5, 89};
    int *ptr = arr;
    int min = *ptr;

    for (int i = 1; i < 5; i++) {
        if (*(ptr + i) < min) {
            min = *(ptr + i);
        }
    }
    printf("Smallest element: %d\n", min);
    return 0;
}
