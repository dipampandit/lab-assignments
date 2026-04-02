// Implement Binary Search using Recursion

#include <stdio.h>

int binarySearch(int arr[], int low, int high, int key) {
    if (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            return mid;
        }
        else if (arr[mid] < key) {
            return binarySearch(arr, mid + 1, high, key);
        }
        else {
            return binarySearch(arr, low, mid - 1, key);
        }
    }
    return -1;
}

int main() {
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Invalid size.");
        return 0;
    }

    int arr[n];
    printf("Enter the elements of the array in sorted order: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int target;
    printf("Enter the number to search: ");
    scanf("%d", &target);

    int ans = binarySearch(arr, 0, n - 1, target);

    if (ans != -1) {
        printf("Element found at index: %d", ans);
    }
    else {
        printf("Element not found.");
    }

    return 0;
}