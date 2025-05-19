#include <stdio.h>

int main(void) {
    int n, i, flag = 1;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter elements:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", arr + i); // pointer way
    }

    int *start = arr, *end = arr + n - 1;
    while(start < end) {
        if(*start != *end) {
            flag = 0;
            break;
        }
        start++;
        end--;
    }

    if(flag)
        printf("Array is a palindrome.\n");
    else
        printf("Array is not a palindrome.\n");

    return 0;
}
