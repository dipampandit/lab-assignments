#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *ptr = arr;

    for (int i = 0; i < 5; i++) {
        printf("Value: %d, Address: %p\n", *(ptr + i), (ptr + i));
    }
    return 0;
}
