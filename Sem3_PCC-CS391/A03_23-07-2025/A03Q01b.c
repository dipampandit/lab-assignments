#include <stdio.h>

int linearSearchPointer(int *ptr, int n, int key) {
    for (int i = 0; i < n; i++) {
        if (*(ptr + i) == key)
            return i; // found
    }
    return -1; // not found
}

int main() {
    int n, key;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter element to search: ");
    scanf("%d", &key);

    int result = linearSearchPointer(arr, n, key);

    if (result != -1)
        printf("Element %d found at index %d\n", key, result);
    else
        printf("Element %d not found\n", key);

    return 0;
}
