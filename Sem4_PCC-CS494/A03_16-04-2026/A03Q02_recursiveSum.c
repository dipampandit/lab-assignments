// Find sum of the elements using divide and conquer method.

#include <stdio.h>

int recursiveSum(int arr[], int low, int high) {
    if (low == high) {
        return arr[low];
    }

    int mid = (low + high) / 2;
    int leftSum = recursiveSum(arr, low, mid);
    int rightSum = recursiveSum(arr, mid + 1, high);

    return leftSum + rightSum;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    int sum = recursiveSum(arr, 0, n - 1);
    printf("Sum: %d\n", sum);

    return 0;
}